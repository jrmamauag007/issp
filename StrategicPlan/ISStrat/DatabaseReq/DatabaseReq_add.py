from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


def DatabaseReq_add(driver):
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    IS = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/p[1]"))
    )
    IS.click()

    DatabaseReq = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[3]/div[1]/div/button"))
    )
    DatabaseReq.click()

    # Fill out the form fields
    form_data_list = [
        {
            "name": "database",
            "description": "description",
            "served": "IS2",
            "from": "2000",
            "to": "2002",
            "status": "For Build-up",
            "archive": "server",
            "owner": "jeb",
            "internal": "group1",
            "external": "group2"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Name of Database']"))
                ), "Database field name not found"
                print("Database field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Description']"))
                ), "Description field name not found"
                print("Description field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Information System/s Served']"))
                ), "IS Served field name not found"
                print("IS Served field name is visible")


                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Implementation Schedule']"))
                ), "Schedule field name not found"
                print("Schedule field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Status']"))
                ), "Status field name not found"
                print("Status field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Data Archiving / Storage Media']"))
                ), "Data archiving field name not found"
                print("Data archiving field name is visible")


                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Owner']"))
                ), "Owner field name not found"
                print("Owner field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Internal Users']"))
                ), "Internal Users field name not found"
                print("Internal Users field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='External Users']"))
                ), "External Users field name not found"
                print("External Users field name is visible")

            except AssertionError as e:
                print(e)

            name_field = driver.find_element(By.XPATH, "//input[@id='is_db_name']")
            name_field.clear()
            name_field.send_keys(form_data["name"])

            description_field = driver.find_element(By.XPATH, "//textarea[@id='is_db_description']")
            description_field.clear()
            description_field.send_keys(form_data["description"])

            IS_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter IS Served']")
            IS_field.clear()
            IS_field.send_keys(form_data["served"])
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            from_field = driver.find_element(By.XPATH, "//input[@placeholder='From']")
            from_field.click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "dp__menu"))
            )
            # Locate the year element (e.g., 1900) and click it
            year_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell' and @data-test='2000']"))
            )
            year_element.click()

            # Locate the "Select" button and click it
            select_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='dp__action_button dp__action_select' and @data-test='select-button']"))
            )
            select_button.click()

            to_field = driver.find_element(By.XPATH, "//input[@placeholder='To']")
            to_field.click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "dp__menu"))
            )
            # Locate the year element (e.g., 1900) and click it
            year_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell' and @data-test='2000']"))
            )
            year_element.click()

            # Locate the "Select" button and click it
            select_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='dp__action_button dp__action_select' and @data-test='select-button']"))
            )
            select_button.click()

            archive_field = driver.find_element(By.XPATH, "//input[@id='is_db_data_archiving']")
            archive_field.clear()
            archive_field.send_keys(form_data["archive"])

            owner_field = driver.find_element(By.XPATH, "//input[@id='is_db_owner']")
            owner_field.clear()
            owner_field.send_keys(form_data["owner"])

            internal_field = driver.find_element(By.XPATH, "//input[@id='is_db_int_users']")
            internal_field.clear()
            internal_field.send_keys(form_data["internal"])

            external_field = driver.find_element(By.XPATH, "//input[@id='is_db_ext_users']")
            external_field.clear()
            external_field.send_keys(form_data["external"])

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/form/div[11]/button"))
            )
            assert save_button.is_displayed(), "Save button is not visible"
            assert save_button.text == "Save", "Save button text is incorrect"
            print(f"'Save' button is visible with text: {save_button.text}")
            save_button.click()

            # Wait for the success message element
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'swal2-title'))
            )
            # Check the actual text against expected text
            actual_text = success_message.text.strip()  # Strip whitespace for accurate comparison
            expected_text = "Database Required added successfully."

            if actual_text == expected_text:
                # Find and click the OK button
                ok_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
                )
                assert ok_button.is_displayed(), "OK button is not visible"
                assert ok_button.text == "OK", "OK button text is incorrect"
                print(f"'OK' button is visible with text: {ok_button.text}")
                ok_button.click()
                print(f"Input success for data: {form_data}")
            else:
                print(f"Input failed for data: {form_data}")
                raise Exception(f"Unexpected success message: {actual_text}")
                # Handle the exception (e.g., if success message not found)
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
