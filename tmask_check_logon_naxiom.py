# Sprawdz po zalogowaniu czy strona ma odpowiedni tytul

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

def test_login():
    driver.get("https://naxiom.tech-com.pl/Identity/Account/Login")
    
    # Wylaczenie komunikatu o nieoryginalnym certyfikacie SSL
    nossl = driver.find_element(By.XPATH, '//*[@id="details-button"]')
    nossl.click()

    nossl = driver.find_element(By.XPATH, '//*[@id="proceed-link"]')
    nossl.click()
    
    # Logowanie
    logonweb = driver.find_element(By.XPATH, '//*[@id="Input_UserName"]')
    logonweb.clear()
    logonweb.send_keys("login")

    logonweb = driver.find_element(By.XPATH, '//*[@id="Input_Password"]')
    logonweb.clear()
    logonweb.send_keys("hasło")

    logonweb = driver.find_element(By.XPATH, '//*[@id="btn-login"]')
    logonweb.click()
     
    get_title = driver.title
    assert "nAxiom" in get_title

def test_down():
    driver.close()
    driver.quit()


def main():
    test_setup()
    test_login()
    test_down()
    print("Test Completed")

if __name__ == "__main__":
    main()
