from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def agency_add(driver):
    # Go to library
    library = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[5]/a"))
    )
    library.click()

    agency = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[1]/p"))
    )
    agency.click()

    # Fill out the form fields
    form_data_list = [
        {
            "agency_name": "Test Agency",
            "alias": "TA",
            "agency_group": "Sectoral Planning Councils",
            "agency_website": "http://www.testagency.com",
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
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div[class='flex flex-row justify-center items-center gap-2'] span"))
            )
            assert add_button.is_displayed(), "Add New button is not visible"
            assert add_button.text == "Add New", "Add New button text is incorrect"
            print(f"'Add New' button is visible")
            add_button.click()

            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Name of Agency']"))
                ), "Name of Agency field name not found"
                print("Name of Agency field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//i[normalize-space()='(short name)']"))
                ), "Alias field name not found"
                print("Alias field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Agency Group']"))
                ), "Agency Group field name not found"
                print("Agency Group field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Agency Official Website Link']"))
                ), "Agency Website field name not found"
                print("Agency Official Website Link field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Name of Agency Head']"))
                ), "Agency Head field name not found"
                print("Name of Agency Head field name is visible")

            except AssertionError as e:
                print(e)

            # Locate and fill the Agency Name field
            agency_name_field = driver.find_element(By.XPATH, "//input[@id='agn_name']")
            agency_name_field.clear()
            agency_name_field.send_keys(form_data["agency_name"])

            # Locate and fill the Alias field
            alias_field = driver.find_element(By.XPATH, "//input[@id='agn_code']")
            alias_field.clear()
            alias_field.send_keys(form_data["alias"])

            # Locate and select the Agency Group from the dropdown
            agency_group_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='agn_group']"))
            agency_group_dropdown.select_by_visible_text(form_data["agency_group"])

            # Locate and fill the Agency Website Link field
            agency_website_field = driver.find_element(By.XPATH, "//input[@id='agn_website']")
            agency_website_field.clear()
            agency_website_field.send_keys(form_data["agency_website"])

            # Locate and fill the First Name field of the Agency Head
            first_name_field = driver.find_element(By.XPATH, "//input[@id='agn_head_fname']")
            first_name_field.clear()
            first_name_field.send_keys(form_data["first_name"])

            # Locate and fill the Middle Initial field of the Agency Head
            middle_initial_field = driver.find_element(By.XPATH, "//input[@id='agn_head_mi']")
            middle_initial_field.clear()
            middle_initial_field.send_keys(form_data["middle_initial"])

            # Locate and fill the Surname field of the Agency Head
            surname_field = driver.find_element(By.XPATH, "//input[@id='agn_head_lname']")
            surname_field.clear()
            surname_field.send_keys(form_data["surname"])

            # Locate and fill the Suffix field of the Agency Head
            suffix_field = driver.find_element(By.XPATH, "//input[@id='agn_head_sfx']")
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
            expected_text = "Agency / Institution added successfully."

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
