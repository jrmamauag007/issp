from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def categories_add(driver):
    # Go to library
    library = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/ul/li[5]/a"))
    )
    library.click()

    categories = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[4]/p"))
    )
    categories.click()

    # Fill out the form fields
    form_data_list = [
        {
            "category": "T2"
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
                    EC.visibility_of_element_located((By.XPATH, "//span[@class='flex flex-row label-text']"))
                ), "ICT Item Category field name not found"
                print("ICT Item Category field name is visible")
            except AssertionError as e:
                print(e)

            # Locate and fill the Agency Name field
            category_field = driver.find_element(By.XPATH, "//input[@id='cat_name']")
            category_field.clear()
            category_field.send_keys(form_data["category"])

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
            expected_text = "ICT Item Category added successfully."

            if actual_text == expected_text:
                # Find and click the OK button
                ok_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
                )
                assert ok_button.is_displayed(), "OK button is not visible"
                assert ok_button.text == "OK", "OK button text is incorrect"
                print(f"'OK' button is visible with text: {ok_button.text}")
                ok_button.click()
                print(f"Success Message is correct: {actual_text}")
                print(f"Input success for data: {form_data}")
            else:
                print(f"Input failed for data: {form_data}")
                raise Exception(f"Unexpected success message: {actual_text}")
                # Handle the exception (e.g., if success message not found)
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
