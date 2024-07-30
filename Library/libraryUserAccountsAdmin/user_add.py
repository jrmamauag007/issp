from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def user_add(driver):
    # Go to the specific page where the form is located
    library = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[5]/a"))
    )
    library.click()

    user = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[6]/p"))
    )
    user.click()

    form_data_list = [
        {
            "first_name": "John",
            "middle_initial": "D",
            "surname": "Doe",
            "suffix": "Jr",
            "email": "jrmamauag777@gmail.com",
            "contact": "09163152945",
            "position": "Officer",
            "level": "Office Focal Person"
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
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Employee Name']"))
                ), "Employee Name field name not found"
                print("Employee Name field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Email Address']"))
                ), "Email Address field name not found"
                print("Email Address field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contact Details']"))
                ), "Contact Details field name not found"
                print("Contact Details field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Position']"))
                ), "Position field name not found"
                print("Position field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Access Level']"))
                ), "Access Level field name not found"
                print("Access Level field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Agency']"))
                ), "Agency field name not found"
                print("Agency field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Office']"))
                ), "Office field name not found"
                print("Office field name is visible")

            except AssertionError as e:
                print(e)

            # Fill the form fields

            first_name_field = driver.find_element(By.XPATH, "//input[@id='usr_fname']")
            first_name_field.clear()
            first_name_field.send_keys(form_data["first_name"])

            middle_initial_field = driver.find_element(By.XPATH, "//input[@id='usr_mname']")
            middle_initial_field.clear()
            middle_initial_field.send_keys(form_data["middle_initial"])

            surname_field = driver.find_element(By.XPATH, "//input[@id='usr_lname']")
            surname_field.clear()
            surname_field.send_keys(form_data["surname"])

            suffix_field = driver.find_element(By.XPATH, "//input[@id='usr_sfx']")
            suffix_field.clear()
            suffix_field.send_keys(form_data["suffix"])

            email_field = driver.find_element(By.XPATH, "//input[@id='usr_email']")
            email_field.clear()
            email_field.send_keys(form_data["email"])

            contact_field = driver.find_element(By.XPATH, "//textarea[@id='usr_contact']")
            contact_field.clear()
            contact_field.send_keys(form_data["contact"])

            position_field = driver.find_element(By.XPATH, "//input[@id='usr_position']")
            position_field.clear()
            position_field.send_keys(form_data["position"])

            access_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='usr_level']"))
            access_dropdown.select_by_visible_text(form_data["level"])

            agency_field = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[6]/div[1]/div[1]/div[1]/input[1]")
            agency_field.click()
            time.sleep(2)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            office_field = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[7]/div[1]/div[1]/div[1]/input[1]")
            office_field.click()
            time.sleep(2)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            cancel_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Cancel']"))
            )
            assert cancel_button.is_displayed(), "Cancel button is not visible"
            assert cancel_button.text == "Cancel", "Cancel button text is incorrect"
            print(f"'Cancel' button is visible with text: {cancel_button.text}")

            # Click the save button and handle confirmation
            invite_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Invite']"))
            )
            assert invite_button.is_displayed(), "Invite button is not visible"
            assert invite_button.text == "Invite", "Invite button text is incorrect"
            print(f"'Invite' button is visible with text: {invite_button.text}")
            invite_button.click()

            # Wait for the success message element
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'swal2-title'))
            )
            # Check the actual text against expected text
            actual_text = success_message.text.strip()  # Strip whitespace for accurate comparison
            expected_text = "Invitation Link sent succesfully."

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


