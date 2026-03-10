import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--window-size=1200,800")

    driver = webdriver.Chrome(options=chrome_options)

    # open calculator.html
    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    yield driver

    driver.quit()


@pytest.mark.ui
def test_manual_ui(driver):

    print("\n====================================")
    print("Calculator opened in browser")
    print("You can now test UI manually")
    print("Try operations like:")
    print(" 1 + 2 =")
    print(" 5 * 3 =")
    print(" sqrt 16")
    print(" factorial 5")
    print("Press ENTER in terminal when finished")
    print("====================================\n")

    input("Press ENTER after finishing manual testing...")

    assert True
