import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()

    # CI Safe Options
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # ✅ Selenium Manager handles driver automatically
    driver = webdriver.Chrome(options=chrome_options)

    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    yield driver
    driver.quit()


def click_buttons(driver, buttons):
    for b in buttons:
        driver.find_element(By.ID, b).click()


def get_display(driver):
    return driver.find_element(By.ID, "display").get_attribute("value")


@pytest.mark.ui
def test_add(driver):
    click_buttons(driver, ["1", "+", "2", "="])
    assert get_display(driver) == "3"


@pytest.mark.ui
def test_sub(driver):
    click_buttons(driver, ["5", "-", "3", "="])
    assert get_display(driver) == "2"


@pytest.mark.ui
def test_mul(driver):
    click_buttons(driver, ["4", "*", "2", "="])
    assert get_display(driver) == "8"


@pytest.mark.ui
def test_div(driver):
    click_buttons(driver, ["8", "/", "2", "="])
    assert get_display(driver) == "4"


@pytest.mark.ui
def test_clear(driver):
    click_buttons(driver, ["9", "+", "1"])
    driver.find_element(By.ID, "C").click()
    assert get_display(driver) == ""
