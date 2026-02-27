import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")   # New Chrome headless mode
    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # IMPORTANT: must open HTML file, not .py file
    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path)

    yield driver
    driver.quit()


def click_buttons(driver, buttons):
    for btn in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, btn))
        ).click()


def get_display(driver):
    return driver.find_element(By.ID, "display").get_attribute("value")


@pytest.mark.ui
def test_addition(driver):
    click_buttons(driver, ["C", "1", "+", "2", "="])
    assert get_display(driver) == "3"


@pytest.mark.ui
def test_subtraction(driver):
    click_buttons(driver, ["C", "5", "-", "3", "="])
    assert get_display(driver) == "2"


@pytest.mark.ui
def test_multiplication(driver):
    click_buttons(driver, ["C", "4", "*", "2", "="])
    assert get_display(driver) == "8"


@pytest.mark.ui
def test_division(driver):
    click_buttons(driver, ["C", "8", "/", "2", "="])
    assert get_display(driver) == "4"


@pytest.mark.ui
def test_clear_button(driver):
    click_buttons(driver, ["C", "9", "+", "1"])
    driver.find_element(By.ID, "C").click()
    assert get_display(driver) == ""
