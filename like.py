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
    time.sleep(5)

def tagseach(tag):
    tagurl = 'https://www.instagram.com/explore/tags/'
    driver.get(tagurl+tag)
    time.sleep(8)

#いいね いいね！
def pushnice(nice_num):
    # 人気の投稿の1枚目をクリックしていいねを実行 
    driver.find_element(By.CLASS_NAME,"_aagw").click()
    time.sleep(5)
    driver.find_element(By.TAG_NAME,"a")
    time.sleep(5)

    # いいねボタンを押す
    driver.find_element(By.CLASS_NAME,"_aamw").click()
    time.sleep(5)
    #次の投稿に移動
    driver.find_element(By.CLASS_NAME,"_abl-").click()
    time.sleep(5)

    for i in range(nice_num-1):
        print(i)

        # いいねボタンを押す
        driver.find_element(By.CLASS_NAME,"_aamw").click()
        x = random.randint(0, 5)
        time.sleep(5+x)

        #次の投稿に移動(修正の必要あり)
        driver.find_element(By.CLASS_NAME,"_aaqg._aaqh").click()
        time.sleep(5+x)


if __name__ == "__main__":
    login()
    tagseach("春")
    pushnice(5)