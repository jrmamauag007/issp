from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def loginAgency(driver):
    try:
        driver.maximize_window()

        # Navigate to the login page
        driver.get("http://10.10.99.23/login")

        # Find the username and password input fields
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        # Enter credentials
        username_field.send_keys("jrmamauag777@gmail.com")
        password_field.send_keys("Dost@123")

        # Find and click the login button
        sign_in_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
        )
        sign_in_button.click()

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        driver.quit()
