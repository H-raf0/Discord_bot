import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

global driver

def openBrowser():
    os.system('start open_browser.cmd')
    sleep(1)
    print("browser is now open")


def login():
    driver.find_element(by=By.XPATH, value='//*[@id="uid_5"]').send_keys("achrafelallali123@gmail.com")
    driver.find_element(by=By.XPATH, value='//*[@id="uid_7"]').send_keys("@polomolo12")
    driver.find_element(by=By.XPATH,
                        value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
    print("logged in?")


def checkMsg():
    try:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/nav/ul/div[2]/div[2]/div/div[2]/div')
    except:
        print("no msg or error")
        return False
    else:
        print("msg detected")
        return True

def readMsgs():
    found = False
    while not found:
        try:
            liMsift = driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/nav/ul/div[2]/div[2]/div/div[2]/div')
        except:
            print("can't find other user icon")
        else:
            found = True

    liMsift.click()

    downloadHTML(driver)

    with open("page.txt", 'r', encoding="utf8") as file:
        f = False
        collect = False
        i=0
        target = 'id="message-content-'
        msg = ""
        lastMsg = ""
        text = file.read()
        for char in text:
            if not f:
                if char == target[i]:  # replace 'x' with the character you want to search for
                    i += 1
                    if i == len(target) - 1:
                        f = True
                else:
                    i = 0
            else:
                if collect:
                    if char != '<':
                        msg += char
                    else:
                        lastMsg = msg
                        msg = ""
                        collect = False
                        f = False
                if char == '>':
                    collect = True
    return lastMsg





    """
    msgs = WebDriverWait(driver, 2).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//*[starts-with(@id, 'message-content-')]"))
    )
    msgLst = []
    for e in msgs:
        msgLst.append(e.text)
    
    return msgLst"""

def doAction(action):
    if action[0] == "/":

        if action == "/help":
            msg = "i can help with nothing MF"
        elif action == "/dance":
            msg = "i don t like dancing"
        else:
            msg = "i don't understand"

        writingBar = driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div')
        writingBar.send_keys(msg + Keys.ENTER)
    # quit conversation
    driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/nav/div[2]/ul/li[1]/div/a/div/div[2]').click()

def downloadHTML(driver):
    # get the page source (i.e. HTML) of the web page
    page_source = driver.page_source

    # save the page source to a file
    with open("page.txt", "w", encoding="utf-8") as f:
        f.write(page_source)

if __name__ == "__main__":

    openBrowser()

    PATH = 'C:\\Users\\achra\\OneDrive\\Bureau\\dis\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


    driver.get("https://discord.com/login")

    # login(driver)

    print(driver.title)

    while 1:
        while not checkMsg():
            sleep(1)
        msg = readMsgs()
        print(msg)
        doAction(msg)


    # driver.quit()
