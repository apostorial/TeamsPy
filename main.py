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
print("Google Chrome opened.")
driver.find_element(By.LINK_TEXT, "Sign in").click()
print("Login page joined.")
time.sleep(1)
file2 = open("emailpass.txt", "r")
line2 = file2.readline()
emailPass = line2.split(":")
email = emailPass[0]
password = emailPass[1]

driver.find_element(By.ID, "i0116").send_keys(f"{email}\n")
print("Email pasted.")
time.sleep(5)
pyautogui.write(f"{password}\n")
print("Password pasted.")
time.sleep(1)

if "Stay signed in?" in driver.page_source:
    driver.find_element(By.ID, "idSIButton9").click()
    print("Successfully bypassed 'Stay signed in'.")
else:
    print("'Stay signed in' not found.")
    pass

time.sleep(1)
driver.find_element(By.CLASS_NAME, "_3lIR1LfENBYPLTyCDNhq5k").click()
print("The filter menu successfully opened.")
time.sleep(1)
driver.find_element(By.NAME, "Unread").click()
print("Mails filtered.")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "_2miAFnGHXlWwulyUmLEbzZ").click()
print("Mail opened.")
time.sleep(1)

file3 = open("invitesentence.txt", "r", encoding="utf8")
line3 = file3.readline()

def checkLink():
    try:
        driver.find_element(By.LINK_TEXT, f"{line3}").click()
        print("Joining link found.")
    except NoSuchElementException:
        driver.find_element_by_css_selector('button[aria-label="More mail actions"]').click()
        print("Action menu successfully opened.")
        time.sleep(1)
        driver.find_element(By.NAME, "Mark as read").click()
        print("Mail read.")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "_2miAFnGHXlWwulyUmLEbzZ").click()
        print("Mail opened.")
        checkLink()

checkLink()
time.sleep(2)
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
print("Microsoft Teams is loading.")
time.sleep(35)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
print("Microphone and camera allowed.")
time.sleep(6)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
print("Microphone and camera disabled.")
time.sleep(2)

joinNow = pyautogui.locateOnScreen("images/joinNow.png")
if joinNow is not None:
    joinNowLocation = pyautogui.center(joinNow)
    pyautogui.click(joinNowLocation)
    print("Reunion joined.")

file4 = open("totaltime.txt", "r")
line4 = float(file4.readline())

inReunionTime = line4 * 3600

for i in range(inReunionTime - 1):
    time.sleep(1)
    print(f"{i + 1} seconds passed.")

driver.quit()
print("Reunion left.")
if __name__ == '__main__':
    pass
