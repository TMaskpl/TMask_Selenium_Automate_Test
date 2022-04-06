#!/usr/bin/python

__author__ = "biuro@tmask.pl"
__copyright__ = "Copyright (C) 2022 TMask.pl"
__license__ = "MIT License"
__version__ = "1.0"


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

url = "https://sklep.pgg.pl/"

def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)


def test_login():
    driver.implicitly_wait(10)
    driver.get(url)

    try:
        f = driver.find_element(By.CSS_SELECTOR, '#main > div > div:nth-child(26) > div.col-4.col-md-2.pt-3.text-center > span.text-4.text-red')
        print(driver.title)
        # f = driver.find_element(By.CSS_SELECTOR, '#main > div > div:nth-child(4) > div.col-4.col-md-2.pt-3.text-center > span.text-4.text-green')
        # print(f.text)
        if f.text == "Brak towaru":
            print("Brak towaru")
            os._exit(0)
        else:
            print("Sprawdz dostępność towaru")
            os._exit(1)
    except:
        print("Serwer nie odpowiada")
        pass
    

def test_down():
    driver.close()
    driver.quit()
    print("Test Completed")


def main():
    test_setup()
    test_login()
    test_down()


if __name__ == "__main__":
    main()
