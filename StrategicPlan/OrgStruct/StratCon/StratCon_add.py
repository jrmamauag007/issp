from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


def StratCon_add(driver):
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    os = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[1]/p"))
    )
    os.click()

    stratcon = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add New']"))
    )
    stratcon.click()

    # Fill out the form fields
    form_data_list = [
        {
            "mfo": "1",
            "system": "1",
            "problem": "1",
            "use": "1"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Major Final Output (MFO) / Organizational Outcome']"))
                ), "MFO field name not found"
                print("MFO field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Critical Management / Operating / Business Systems']"))
                ), "System field name not found"
                print("System field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Problems']"))
                ), "Problems field name not found"
                print("Problems field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Intended Use of ICT']"))
                ), "Intended Use field name not found"
                print("Intended Use field name is visible")

            except AssertionError as e:
                print(e)

            mfo_field = driver.find_element(By.XPATH, "//input[@placeholder='Select MFO']")
            mfo_field.clear()
            mfo_field.send_keys(form_data["mfo"])
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            system_field = driver.find_element(By.XPATH, "//textarea[@id='critical_mngt']")
            system_field.clear()
            system_field.send_keys(form_data["system"])

            problem_field = driver.find_element(By.XPATH, "//textarea[@id='problem']")
            problem_field.clear()
            problem_field.send_keys(form_data["problem"])

            use_field = driver.find_element(By.XPATH, "//textarea[@id='intended']")
            use_field.clear()
            use_field.send_keys(form_data["use"])

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[6]/button[1]"))
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
            expected_text = "Strategic Concern for ICT Use added successfully."

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
