from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def agency_add(driver):
    # Go to library
    agency = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[2]/a"))
    )
    agency.click()

    profile = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[1]/p"))
    )
    profile.click()

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
            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='IS Planner']"))
                ), "IS Planner field name not found"
                print("IS Planner field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Agency Head']"))
                ), "Agency Head field name not found"
                print("Agency Head field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Focal Person']"))
                ), "Focal Person field name not found"
                print("Focal Person field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Agency Official Website Link']"))
                ), "Agency Official Website Link field name not found"
                print("Agency Official Website Link field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Agency Official Website Link']"))
                ), "Agency Website field name not found"
                print("Agency Official Website Link field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Focal Person Contact Details']"))
                ), "Focal Person Contact Details field name not found"
                print("Focal Person Contact Details field name is visible")


                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='IS Planner']"))
                ), "IS Planner field name not found"
                print("IS Planner field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Designated IS Planner']"))
                ), "Designated IS Planner field name not found"
                print("Designated IS Planner field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Email Address']"))
                ), "Email Address field name not found"
                print("Email Address field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Designated IS Planner']"))
                ), "Designated IS Planner field name not found"
                print("Designated IS Planner field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Plantilla Position']"))
                ), "Plantilla Position field name not found"
                print("Plantilla Position field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contact Number']"))
                ), "Contact Number field name not found"
                print("Contact Number field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()=' Organizational Chart ']"))
                ), "Organizational Chart field name not found"
                print("Organizational Chart field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='No. of Regional/Extension Offices']"))
                ), "No. of Regional/Extension Offices field name not found"
                print("No. of Regional/Extension Offices field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='No. of Provincial Offices']"))
                ), "No. of Provincial Offices field name not found"
                print("No. of Provincial Offices field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='No. of Other Offices']"))
                ), "No. of Other Offices field name not found"
                print("No. of Other Offices field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='No. of Actual Plantilla Positions']"))
                ), "No. of Actual Plantilla Positions field name not found"
                print("No. of Actual Plantilla Positions field name is visible")

            except AssertionError as e:
                print(e)

            reg_field = driver.find_element(By.XPATH, "//input[@id='oc_no_reg_offices']")
            reg_field.clear()
            reg_field.send_keys(form_data["reg"])

            prov_field = driver.find_element(By.XPATH, "//input[@id='oc_no_prov_offices']")
            prov_field.clear()
            prov_field.send_keys(form_data["prov"])

            other_field = driver.find_element(By.XPATH, "//input[@id='oc_no_other_offices']")
            other_field.clear()
            other_field.send_keys(form_data["other"])

            actual_field = driver.find_element(By.XPATH, "//input[@id='oc_no_actual_plntlla_pos']")
            actual_field.clear()
            actual_field.send_keys(form_data["actual"])

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
