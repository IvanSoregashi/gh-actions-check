import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import pytest

url = "http://" + os.getenv("JENKINS_HOST") + ":" + os.getenv("JENKINS_PORT") + "/"


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.find_element(By.NAME, "j_username").send_keys(os.getenv("JENKINS_USERNAME"))
    driver.find_element(By.NAME, "j_password").send_keys(os.getenv("JENKINS_PASSWORD"))
    driver.find_element(By.NAME, "Submit").click()
    time.sleep(2)
    yield driver
    driver.quit()

def test_jenkins(driver):
    assert driver.current_url == "http://localhost:8080/"

def test_item(driver):
    element = driver.find_element(By.LINK_TEXT, "Test item")
    assert element.get_attribute("href") == "http://localhost:8080/job/Test%20item/"
