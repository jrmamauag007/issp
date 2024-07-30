from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

# Use forward slashes which work on all operating systems
library_path = 'C:/Users/jrmam/test/pythonProject/Library'
sys.path.insert(0, library_path)

from loginAgency import loginAgency
from userAgency_add import userAgency_add

def main():
    # Initialize the browser driver
    driver_path = r"C:\Users\jrmam\test\pythonProject\Library\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Execute test cases
        loginAgency(driver)
        userAgency_add(driver)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
