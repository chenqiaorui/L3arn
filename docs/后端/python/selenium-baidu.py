# coding=utf-8

# 最新版的selenium(4.x.x)已经不支持PhantomJS。如要用PhantomJS，可用旧版本selenium。如pip install selenium==3.8.0。
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

# browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)



def search():
    try:
        print('开始访问百度....')
        browser.get("https://www.baidu.com/")

        
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#kw")))
        submit = WAIT.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#su")))

        input.send_keys('蔡徐坤 篮球')
        submit.click()

       
    except TimeoutException:
        return search()

def main():
    try:
        search()
        

    finally:
        browser.close()


if __name__ == '__main__':
    main()
    
