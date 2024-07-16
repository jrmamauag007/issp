from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
import os

agency_path = 'C:/Users/jrmam/test/pythonProject/StrategicPlan'
sys.path.insert(0, agency_path)

from login import login
from ProposedIS_add import ProposedIS_add

def main():
    # Initialize the browser driver
    driver_path = r"C:\Users\jrmam\test\pythonProject\StrategicPlan\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Execute test cases
        login(driver)
        ProposedIS_add(driver)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
