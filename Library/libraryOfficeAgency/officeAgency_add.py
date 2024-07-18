from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def officeAgency_add(driver):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[1]/a"))
    )
    driver.get("http://10.10.99.23/library")

    # Form data
    form_data_list = [
        {
            "office_name": "Planning and Evaluation Service20",
            "alias": "PES",
            "first_name": "John",
            "middle_initial": "D",
            "surname": "Doe",
            "suffix": "Jr."
        }
    ]

    for form_data in form_data_list:
        try:
            # Click the "Add New" button
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='flex flex-row justify-center items-center gap-2'] span"))
            )
            assert add_button.is_displayed(), "Add New button is not visible"
            assert add_button.text == "Add New", "Add New button text is incorrect"
            print(f"'Add New' button is visible")
            add_button.click()

            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Parent Office']"))
                ), "Parent Office label field name not found"
                print("Parent Office label field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Name of Office']"))
                ), "Name of Office field name not found"
                print("Name of Office field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//i[normalize-space()='(short name)']"))
                ), "Alias(shortname) field name not found"
                print("Alias(shortname) field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Name of Office Head']"))
                ), "Name of Office Head field name not found"
                print("Name of Office Head field name is visible")

            except AssertionError as e:
                print(e)

            # Fill the form fields

            input_field = driver.find_element(By.CLASS_NAME, "vs__search")
            input_field.click()
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            office_name_field = driver.find_element(By.XPATH, "//input[@id='ofc_name']")
            office_name_field.clear()
            office_name_field.send_keys(form_data["office_name"])

            alias_field = driver.find_element(By.XPATH, "//input[@id='ofc_code']")
            alias_field.clear()
            alias_field.send_keys(form_data["alias"])

            first_name_field = driver.find_element(By.XPATH, "//input[@id='ofc_head_fname']")
            first_name_field.clear()
            first_name_field.send_keys(form_data["first_name"])

            middle_initial_field = driver.find_element(By.XPATH, "//input[@id='ofc_head_mi']")
            middle_initial_field.clear()
            middle_initial_field.send_keys(form_data["middle_initial"])

            surname_field = driver.find_element(By.XPATH, "//input[@id='ofc_head_lname']")
            surname_field.clear()
            surname_field.send_keys(form_data["surname"])

            suffix_field = driver.find_element(By.XPATH, "//input[@id='ofc_head_sfx']")
            suffix_field.clear()
            suffix_field.send_keys(form_data["suffix"])

            cancel_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Cancel']"))
            )
            assert cancel_button.is_displayed(), "Cancel button is not visible"
            assert cancel_button.text == "Cancel", "Cancel button text is incorrect"
            print(f"'Cancel' button is visible with text: {cancel_button.text}")

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
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
            expected_text = "Office added successfully."

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


