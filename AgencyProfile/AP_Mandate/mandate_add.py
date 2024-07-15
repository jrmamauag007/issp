from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def mandate_add(driver):
    # Go to library
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[2]/a"))
    )
    driver.get("http://10.10.99.23/agency-profile")

    mandate = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[2]/a"))
    )
    mandate.click()

    # Fill out the form fields
    form_data_list = [
        {
            "basis": "Test",
            "function": "Test",
            "vision": "Test",
            "mission": "Test",
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Mandate']"))
                ), "Mandate field name not found"
                print("Mandate field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='flex flex-row label-text' and contains(text(),'Legal Basis')]"))
                ), "Legal Basis field name not found"
                print("Legal Basis field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='flex flex-row label-text' and contains(text(),'Functions')]"))
                ), "Functions field name not found"
                print("Functions field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//p[normalize-space()='Vision Statement']"))
                ), "Vision Statement field name not found"
                print("Vision Statement field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='flex flex-row label-text' and contains(text(),'Vision Statement')]"))
                ), "Statement field name not found"
                print("Statement field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Mission Statement']"))
                ), "Mission Statement field name not found"
                print("Mission Statement field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='flex flex-row label-text' and contains(text(),'Mission Statement')]"))
                ), "Statement field name not found"
                print("Statement field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Agency and its Environment (Functional Interface C')]"))
                ), "AGENCY  field name not found"
                print("AGENCY  field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Browse']"))
                ), "Browse button not found"
                print("Browse button is visible")

            except AssertionError as e:
                print(e)

            basis_field = driver.find_element(By.XPATH, "//textarea[@id='agn_legal_basis']")
            basis_field.clear()
            basis_field.send_keys(form_data["basis"])

            function_field = driver.find_element(By.XPATH, "//textarea[@id='agn_functions']")
            function_field.clear()
            function_field.send_keys(form_data["function"])

            vision_field = driver.find_element(By.XPATH, "//textarea[@id='agn_vision']")
            vision_field.clear()
            vision_field.send_keys(form_data["vision"])

            mission_field = driver.find_element(By.XPATH, "//textarea[@id='agn_mission']")
            mission_field.clear()
            mission_field.send_keys(form_data["mission"])

            img_field = driver.find_element(By.XPATH, "//input[@type='file']")
            img_field.send_keys('C:/Users/jrmam/test/pythonProject/AgencyProfile/img.png')

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
            expected_text = "Mandate saved successfully."

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
