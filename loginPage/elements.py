from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser driver
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the login page
    driver.get("http://10.10.99.23/login")

    # Verify the presence of all elements
    elements = [
        (By.XPATH, "//h1[contains(text(), 'System Name')]"),
        (By.XPATH, "//h2[contains(text(), 'Sign In Modal form')]"),
        (By.ID, "email"),
        (By.ID, "password"),
        (By.XPATH, "//button[@type='button']"),
        (By.XPATH, "//input[@type='checkbox' and @name='remember']"),
        (By.LINK_TEXT, "Forgot Password?"),
        (By.XPATH, "//button[contains(text(), 'Sign in')]"),
        (By.XPATH, "//img[@alt='DX Logo']"),
        (By.XPATH, "//p[contains(text(), 'Copyright')]")
    ]

    for locator in elements:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
    print("All elements are present: Test Passed.")

except Exception as e:
    print(f"Test Failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()
