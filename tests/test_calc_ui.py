import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()

    # Run visible browser for manual testing
    chrome_options.add_argument("--window-size=1200,800")

    driver = webdriver.Chrome(options=chrome_options)

    file_path = os.path.abspath("calculator.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    yield driver

    driver.quit()


@pytest.mark.ui
def test_manual_ui(driver):

    # Skip in CI environments like Jenkins
    if os.environ.get("JENKINS_HOME"):
        pytest.skip("Skipping manual UI test in CI environment")

    print("\n====================================")
    print("Calculator opened in browser")
    print("Test UI manually now")
    print("Try examples:")
    print("1 + 2 =")
    print("5 * 3 =")
    print("sqrt 16")
    print("factorial 5")
    print("Browser will stay open for 60 seconds")
    print("====================================\n")

    # wait for manual interaction
    time.sleep(60)

    assert True
