import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # Assumes chromedriver is in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open local dashboard file
    file_path = os.path.abspath("dashboard.py")
    driver.get("file:///" + file_path)

    yield driver
    driver.quit()


def click_buttons(driver, buttons):
    for btn in buttons:
        driver.find_element(By.ID, btn).click()


def get_display(driver):
    return driver.find_element(By.ID, "display").get_attribute("value")


# 1️⃣ Addition Test
@pytest.mark.ui
def test_addition(driver):
    click_buttons(driver, ["1", "+", "2", "="])
    assert get_display(driver) == "3"


# 2️⃣ Subtraction Test
@pytest.mark.ui
def test_subtraction(driver):
    click_buttons(driver, ["5", "-", "3", "="])
    assert get_display(driver) == "2"


# 3️⃣ Multiplication Test
@pytest.mark.ui
def test_multiplication(driver):
    click_buttons(driver, ["4", "*", "2", "="])
    assert get_display(driver) == "8"


# 4️⃣ Division Test
@pytest.mark.ui
def test_division(driver):
    click_buttons(driver, ["8", "/", "2", "="])
    assert get_display(driver) == "4"


# 5️⃣ Clear Button Test
@pytest.mark.ui
def test_clear_button(driver):
    click_buttons(driver, ["9", "+", "1"])
    driver.find_element(By.ID, "C").click()
    assert get_display(driver) == ""
