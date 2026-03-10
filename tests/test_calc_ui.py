import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    yield driver
    driver.quit()


# Helper Functions

def click_buttons(driver, buttons):
    for button in buttons:
        driver.find_element(By.ID, button).click()


def get_display(driver):
    return driver.find_element(By.ID, "display").get_attribute("value")


def clear_display(driver):
    driver.find_element(By.ID, "C").click()


# Calculator Operation Tests

@pytest.mark.ui
@pytest.mark.parametrize("buttons, expected", [
    (["1", "+", "2", "="], "3"),
    (["5", "-", "3", "="], "2"),
    (["4", "*", "2", "="], "8"),
    (["8", "/", "2", "="], "4"),
])
def test_calculator_operations(driver, buttons, expected):

    clear_display(driver)   # 🔹 important fix

    click_buttons(driver, buttons)

    assert get_display(driver) == expected


# Clear Button Test

@pytest.mark.ui
def test_clear(driver):

    click_buttons(driver, ["9", "+", "1"])

    clear_display(driver)

    assert get_display(driver) == ""
