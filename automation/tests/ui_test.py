import pytest
from selenium import webdriver
import time

def test_google_title():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(2)
    assert "Google" in driver.title
    driver.quit()
    