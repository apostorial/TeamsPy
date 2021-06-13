import selenium
import time
import datetime
import pyautogui
import selenium.webdriver.common.alert
from datetime import datetime
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

file1 = open("time.txt", "r")
line1 = file1.readline()

secondsPassed = 0

while True:
    date = datetime.now()
    hour =f"{date.hour:02d}"
    minute = f"{date.minute:02d}"
    seconds = f"{date.second:02d}"
    if line1 == f"{hour}:{minute}":
        break
    print("Waiting...")
    time.sleep(30)
    secondsPassed += 30
    print(f"Time passed: {secondsPassed} seconds")
    print(f"Current time: {hour}:{minute}:{seconds}")

driver = Chrome()

driver.get("https://outlook.live.com/owa/")

driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(1)
file2 = open("emailpass.txt", "r")
line2 = file2.readline()
emailPass = line2.split(":")
email = emailPass[0]
password = emailPass[1]

driver.find_element(By.ID, "i0116").send_keys(f"{email}\n")
time.sleep(5)
pyautogui.write(f"{password}\n")
time.sleep(1)

if "Stay signed in?" in driver.page_source:
    driver.find_element(By.ID, "idSIButton9").click()
else:
    pass

time.sleep(1)
driver.find_element(By.CLASS_NAME, "_3lIR1LfENBYPLTyCDNhq5k").click()
time.sleep(1)
driver.find_element(By.NAME, "Unread").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "_2miAFnGHXlWwulyUmLEbzZ").click()
time.sleep(1)

file3 = open("invitesentence.txt", "r", encoding="utf8")
line3 = file3.readline()

def checkLink():
    try:
        driver.find_element(By.LINK_TEXT, f"{line3}").click()
    except NoSuchElementException:
        driver.find_element_by_css_selector('button[aria-label="More mail actions"]').click()
        time.sleep(1)
        driver.find_element(By.NAME, "Mark as read").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "_2miAFnGHXlWwulyUmLEbzZ").click()
        checkLink()

checkLink()
time.sleep(2)
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(35)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

joinNow = pyautogui.locateOnScreen("images/joinNow.png")
if joinNow is not None:
    joinNowLocation = pyautogui.center(joinNow)
    pyautogui.click(joinNowLocation)

if __name__ == '__main__':
    pass