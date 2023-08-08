import logging
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_katalon_booking():
    log = logging.getLogger(__name__)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    time.sleep(2)
    username = driver.find_element(By.ID, "txt-username")
    time.sleep(2)
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    login_btn = driver.find_element(By.ID, "btn-login")
    login_btn.click()
    time.sleep(2)

    drop_down = Select(driver.find_element(By.ID, "combo_facility"))
    drop_down.select_by_visible_text("Seoul CURA Healthcare Center")

    checkbox = driver.find_element(By.ID, "chk_hospotal_readmission")
    checkbox.click()

    radio_button = driver.find_element(By.NAME, "programs")
    radio_button.click()

    date = driver.find_element(By.ID, "txt_visit_date")
    date.send_keys("23/08/2023")

    comment = driver.find_element(By.ID, "txt_comment")
    comment.send_keys("Future Booking for Mr Chinmay")

    appointment_btn = driver.find_element(By.ID, "btn-book-appointment")
    appointment_btn.click()
    time.sleep(3)

    heading_h2 = driver.find_element(By.TAG_NAME,"h2")

    assert "Appointment Confirmation" in heading_h2.text
