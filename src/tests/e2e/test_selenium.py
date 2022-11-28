import socket
from selenium  import webdriver
import time
import pytest
from selenium.webdriver.common.by import By



options = webdriver.FirefoxOptions()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options,
    )




def _local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        try:
            return s.getsockname()[0]
        finally:
            s.close()

url = f"http://{_local_ip()}:48800"



def test_website():


    assert driver != None

    driver.get(url)

    assert len(driver.title) > 0

    btn_login = driver.find_element(By.ID, "test_login")
    btn_login.click()

    assert driver.current_url == f"{url}/auth/login"


    #driver.get(url)

    btn_reg = driver.find_element(By.ID, "test_register")
    btn_reg.click()

    assert driver.current_url == f"{url}/auth/register"

    
    driver.quit()

