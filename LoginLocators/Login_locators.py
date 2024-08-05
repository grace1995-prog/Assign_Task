from selenium.webdriver.common.by import By


class Login_locators:
    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


class NegativeLoginPageLocators:
    USERNAME_ = (By.NAME, "user-name")
    PASSWORD_ = (By.NAME, "password")
    LOGIN_BUTTON_ = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3')
