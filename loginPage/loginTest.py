from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# List of credentials to test
credentials_list = [
    {"username": "admin@gmail.com", "password": "Dost@123"},
    # {"username": "agency@dost.gov.ph", "password": "Dost@123"},
    # {"username": "anotheruser@example.com", "password": "Password123"},
    # {"username": " ", "password": " "}
    # Add more credentials as needed
]

# Initialize the browser driver
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Iterate through each set of credentials
for credentials in credentials_list:
    try:
        # Navigate to the login page
        driver.get("http://10.10.99.23/login")

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Email Address']"))
        ), "Email Address label not found"
        print("Email Address label is visible")

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Password']"))
        ), "Password label not found"
        print("Password label is visible")

        # Find the username and password input fields
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        # Enter credentials
        username_field.send_keys(credentials["username"])
        password_field.send_keys(credentials["password"])

        # Find and click the login button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
        )
        assert sign_in_button.is_displayed(), "Sign in button is not visible"
        assert sign_in_button.text == "Sign in", "Sign in button text is incorrect"
        sign_in_button.click()

        # Wait for a while to let the login process complete
        time.sleep(5)

        # Check if login was successful by verifying the presence of a logout button
        WebDriverWait(driver, 30).until(lambda d: d.current_url != "http://10.10.99.23/login")
        time.sleep(2)
        print(f"Login successful for {credentials['username']}")

    except Exception as e:
        print(f"Login failed for {credentials['username']}")
        print(f"Exception occurred: {str(e)}")
        driver.quit()

# Close the browser at the end of all iterations
driver.quit()
