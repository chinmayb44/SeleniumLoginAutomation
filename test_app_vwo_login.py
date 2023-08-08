import logging
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time


def test_app_vwo_login_invalid():
    log = logging.getLogger(__name__)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    username = driver.find_element(By.ID, "login-username")
    username.send_keys("abc@gmail.com")

    password = driver.find_element(By.ID, "login-password")
    password.send_keys("1234")

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()
    time.sleep(5)
    notification_msg = driver.find_element(By.ID, "js-notification-box-msg")

    assert "Your email, password, IP address or location did not match" in notification_msg.text
    print(notification_msg.text)


def test_app_vwo_login_valid():
    log = logging.getLogger(__name__)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    username = driver.find_element(By.ID, "login-username")
    username.send_keys("93npu2yyb0@esiix.com")

    password = driver.find_element(By.ID, "login-password")
    password.send_keys("Wingify@123")

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()
    time.sleep(5)
    log.info('title is ' + driver.title)
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.back()
    driver.get("https://sdet.live")
    driver.forward()
