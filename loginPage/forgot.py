from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser driver
service = Service('C:/Users/jrmam/test/pythonProject/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the login page
    driver.get("http://10.10.99.23/login")

    # Click on the "Forgot Password?" link
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot Password?"))
    )
    forgot_password_link.click()

    # Verify that the user is redirected to the password reset page
    WebDriverWait(driver, 10).until(
        EC.url_contains("reset-password")
    )

    # Enter a registered email address
    driver.find_element(By.ID, "email").send_keys("admin@gmail.com")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Reset Password')]").click()

    # Verify that the reset process starts (e.g., a confirmation message is displayed)
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'check your email')]"))
    )
    assert confirmation_message.is_displayed(), "Password reset failed: Confirmation message not found."

    print("Password reset process initiated: Test Passed.")

except Exception as e:
    print(f"Test Failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()
