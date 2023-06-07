from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import random

driver = webdriver.Chrome()

# ログイン
def login():
    # メアドとパスワードを入力
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(2)
    driver.find_element(By.NAME,"username").send_keys("riku0810ma@yahoo.ne.jp")
    time.sleep(1)
    driver.find_element(By.NAME,"password").send_keys("ma3874266")
    time.sleep(2)

    # ログインボタンを押す
    driver.find_element(By.CLASS_NAME,"_acan._acap._acas._aj1-").click()
    time.sleep(5)

    #後で
    driver.find_element(By.CLASS_NAME,"_ac8f").click()
    time.sleep(5)

    #後で
    driver.find_element(By.CLASS_NAME,"_a9--._a9_1").click()
    time.sleep(10)

def serchplof():
    #driver.find_element(By.CLASS_NAME,"x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd").click()
    username_url = f"https://www.instagram.com/{username}/followers/"
    driver.get(username_url)
    time.sleep(5)

    #driver.find_element(By.CLASS_NAME,"x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd").click()

if __name__ == "__main__":
    login()
    username = "kurida_ema"
    serchplof()