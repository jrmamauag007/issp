from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def agency_search(driver):
    # Go to library
    library = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[5]/a"))
    )
    library.click()

    search_terms = ["FNRI", "Food", "Renato", "google.com"," ", "12345"," 12 345","FN RI"]

    for search_term in search_terms:
        try:
            # Enter search term in the search box
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @placeholder='Search...']"))
            )

            search_box.clear()

            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)

            # Verify that the table records are filtered based on the search term
            filtered_records = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, f"//td[contains(text(), '{search_term}')]"))
            )
            print(f"Results show for search term: {search_term}")

        except Exception as e:
            print(f"No records found matching the search term.")

        time.sleep(5)


