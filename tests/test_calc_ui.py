import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("http://localhost:5000")
    yield driver
    driver.quit()


# =========================
# SMOKE TESTS
# =========================

@pytest.mark.smoke
def test_addition_ui(driver):
    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("3")
    Select(driver.find_element(By.ID, "operator")).select_by_value("+")
    driver.find_element(By.ID, "calculate").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "8"


@pytest.mark.smoke
def test_subtraction_ui(driver):
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("4")
    Select(driver.find_element(By.ID, "operator")).select_by_value("-")
    driver.find_element(By.ID, "calculate").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "6"


# =========================
# SLOW TESTS
# =========================

@pytest.mark.slow
def test_large_number_addition(driver):
    driver.find_element(By.ID, "num1").send_keys("9999999")
    driver.find_element(By.ID, "num2").send_keys("1")
    Select(driver.find_element(By.ID, "operator")).select_by_value("+")
    driver.find_element(By.ID, "calculate").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "10000000"


@pytest.mark.slow
def test_multiple_operations_refresh(driver):
    for _ in range(3):
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        driver.find_element(By.ID, "num1").send_keys("2")
        driver.find_element(By.ID, "num2").send_keys("2")
        Select(driver.find_element(By.ID, "operator")).select_by_value("*")
        driver.find_element(By.ID, "calculate").click()
        assert driver.find_element(By.ID, "result").text == "4"


# =========================
# SECURITY TESTS
# =========================

@pytest.mark.security
def test_script_injection(driver):
    driver.find_element(By.ID, "num1").send_keys("<script>")
    driver.find_element(By.ID, "num2").send_keys("5")
    Select(driver.find_element(By.ID, "operator")).select_by_value("+")
    driver.find_element(By.ID, "calculate").click()
    result = driver.find_element(By.ID, "result").text
    assert "error" in result.lower()


@pytest.mark.security
def test_sql_injection(driver):
    driver.find_element(By.ID, "num1").send_keys("1; DROP TABLE")
    driver.find_element(By.ID, "num2").send_keys("2")
    Select(driver.find_element(By.ID, "operator")).select_by_value("+")
    driver.find_element(By.ID, "calculate").click()
    result = driver.find_element(By.ID, "result").text
    assert "error" in result.lower()
