import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginLocators.Login_locators import Login_locators, NegativeLoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.PASSWORD))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.LOGIN_BUTTON))
        click_login_button.click()


class LoginPage1:
    def __init__(self, driver):
        self.driver = driver

    def login_urls(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.USERNAME_))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.PASSWORD_))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.LOGIN_BUTTON_))
        click_login_button.click()
        time.sleep(5)

    def get_error_message_element(self):
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NegativeLoginPageLocators.ERROR_MESSAGE))

        return error_message_element
