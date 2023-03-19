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
        driver.find_element(by=By.CSS_SELECTOR,
                            value='#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div > nav > ul > div.scroller-3X7KbA.none-1rXy4P.scrollerBase-1Pkza4 > div:nth-child(2)')
    except:
        print("no msg or error")
        return False
    else:
        print("msg detected")
        return True

def readMsgs():
    liMsift = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#app-mount > div.appAsidePanelWrapper-ev4hlp > div.notAppAsidePanel-3yzkgB > div.app-3xd6d0 > div > div.layers-OrUESM.layers-1YQhyW > div > div > nav > ul > div.scroller-3X7KbA.none-1rXy4P.scrollerBase-1Pkza4 > div:nth-child(2)'))
    )

    liMsift.click()
    msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//*[starts-with(@id, 'message-content-')]"))
    )
    msgLst = []
    for e in msg:
        msgLst.append(e.text)
        # print(e.text)
    return msgLst

def doAction(action):
    if action == "/help":
        msg = "i can help with nothing MF"
    elif action == "/dance":
        msg = "i don t like dancing"
    else:
        msg = "i don't understand"

    writingBar = driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div')
    writingBar.send_keys(msg + Keys.ENTER)


if __name__ == "__main__":

    openBrowser()

    PATH = 'C:\\Users\\achra\\OneDrive\\Bureau\\dis\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


    driver.get("https://discord.com/login")

    # login(driver)

    print(driver.title)

    while not checkMsg():
        sleep(1)


    msglst = readMsgs()

    doAction(msglst[-1])


    driver.quit()
