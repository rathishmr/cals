import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path)
    yield driver
    driver.quit()

def click_buttons(driver, buttons):
    for btn in buttons:
        driver.find_element(By.XPATH, f"//button[text()='{btn}']").click()

def get_display(driver):
    return driver.find_element(By.ID, "display").get_attribute("value")

@pytest.mark.ui
def test_addition(driver):
    click_buttons(driver, ["1", "+", "2", "="])
    assert get_display(driver) == "3"

@pytest.mark.ui
def test_subtraction(driver):
    click_buttons(driver, ["5", "-", "3", "="])
    assert get_display(driver) == "2"

@pytest.mark.ui
def test_multiplication(driver):
    click_buttons(driver, ["4", "*", "2", "="])
    assert get_display(driver) == "8"

@pytest.mark.ui
def test_division(driver):
    click_buttons(driver, ["8", "/", "2", "="])
    assert get_display(driver) == "4"

@pytest.mark.ui
def test_clear_button(driver):
    click_buttons(driver, ["9", "+", "1"])
    driver.find_element(By.ID, "C").click()
    assert get_display(driver) == ""
