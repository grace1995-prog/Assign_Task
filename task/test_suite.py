import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from loginPage.login_page_test import LoginPage, LoginPage1


# To run on normal browser
@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://www.saucedemo.com")
    return login_page


def test_login_page_on_sauce_demo_website(login):
    login.enter_username("performance_glitch_user")
    login.enter_password("secret_sauce")
    login.click_login_button()


@pytest.fixture(scope="module")
def driver_setup1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_gbp(driver_setup1):
    driver = driver_setup1
    login_page = LoginPage1(driver)
    login_page.login_urls("https://www.saucedemo.com")
    return login_page


def test_negative_login_on_sauce_demo_website(login_gbp):
    login_gbp.enter_username("performance_glitch_user")
    login_gbp.enter_password("secret_sacejk")
    login_gbp.click_login_button()

    # Verify the error message
    error_message_element = login_gbp.get_error_message_element()
    error_message = error_message_element.text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, \
        "Error message does not match expected."

    print("Negative test passed: Username and password do not match any user in this service.")
