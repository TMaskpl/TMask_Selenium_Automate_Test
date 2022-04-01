#!/usr/bin/python

__author__ = "biuro@tmask.pl"
__copyright__ = "Copyright (C) 2022 TMask.pl"
__license__ = "MIT License"
__version__ = "1.0"

# Sprawdzenie pliku w VirusTotal - max 650 Mb
# Run
# python tmask_virustotal.py <Sciezka do pliku>

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import sys

def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()

def test_virustotal():
    var1 = sys.argv[1]
    print(var1)
    path = os.path.abspath(var1)
    def open_shadow_root(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    driver.implicitly_wait(60)
    driver.get("https://www.virustotal.com/gui/home/upload")
    root_1 = driver.find_element(By.CSS_SELECTOR, "#view-container > home-view")
    sroot_1 = open_shadow_root(root_1)
    root_2 = sroot_1.find_element(By.CSS_SELECTOR, "#uploadForm")
    sroot_2 = open_shadow_root(root_2)
    file_element = sroot_2.find_element(By.CSS_SELECTOR, "#fileSelector")
    file_element.send_keys(var1)
    root_3 = sroot_2.find_element(By.CSS_SELECTOR, "#confirmUpload")
    root_3.click()

def test_down():
    # driver.close()
    # driver.quit()
    print("Test Completed")


def main():
    test_setup()
    test_virustotal()
    test_down()


if __name__ == "__main__":
    main()
