from selenium import webdriver
from selenium.webdriver.chrome.service import Service

library_path = 'C:/Users/jrmam/test/pythonProject/Library'
sys.path.insert(0, library_path)

from login import login
from agency_add import agency_add

def main():
    # Initialize the browser driver
    driver_path = r"C:\Users\jrmam\test\pythonProject\Library\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Execute test cases
        login(driver)
        print("login success")

        # agency_search(driver)
        # print("search success")

        agency_add(driver)
        print("add success")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
