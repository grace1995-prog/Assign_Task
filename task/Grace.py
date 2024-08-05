import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    # Find the username and password input fields
    username_field = driver.find_element(By.NAME, "user-name")
    password_field = driver.find_element(By.NAME, "password")

    # Enter invalid credentials
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauc")

    # Find and click the login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for the error message to be displayed
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3'))
    )

    # Verify the error message
    error_message = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
    assert "Invalid credentials" in error_message, ("Epic sadface: Username and password do not match any user in this "
                                                    "service.")

    print("Negative test passed: Epic sadface: Username and password do not match any user in this service.")
except Exception as e:
    print(f"Negative test passed: {e}")

# Close the browser
driver.quit()

driver = webdriver.Chrome()
# Navigate to the login page
driver.get("https://www.saucedemo.com")
driver.maximize_window()

# Find the username and password input fields
username_field = driver.find_element(By.NAME, "user-name")
password_field = driver.find_element(By.NAME, "password")

# Enter invalid credentials
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

# Find and click the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(20)

# Close the browser
driver.quit()
