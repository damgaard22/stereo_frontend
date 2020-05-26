from selenium import webdriver
import time
import sys
import datetime
from PyQt5.QtWidgets import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/local/bin/chromedriver')

driver.get("https://tradingsim.com/simulator/")


try:
    element = WebDriverWait(driver, 200).until(
        EC.title_contains('TradingSim')
    )

except:
    driver.quit()


def get_replay_time(driver):
    time = driver.find_element_by_xpath('//div[contains(@class, "bubble value low")]').text
    if not time:
        return ''

    if len(time.split(':')) < 3:
        time += ':00'

    parts = time.split(':')
    time = datetime.time(int(parts[0]), int(parts[1]), int(parts[2]))
    return time


while True:
    time.sleep(0.25)
    replay_time = driver.execute_script("return ReplayModelInstance.replayTime()")
    if replay_time:
        replay_time = datetime.datetime.fromtimestamp(replay_time/1000) - datetime.timedelta(hours=6)
    else:
        continue
    f = open('time.txt', 'w')
    f.write(replay_time.strftime("%H:%M:%S %d-%m-%Y"))
    f.close()
    print(replay_time)




