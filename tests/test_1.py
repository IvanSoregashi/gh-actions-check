def test_1():
    assert True

def test_3():
    assert True

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_34():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://example.com")

    assert driver.current_url == "http://example.com"