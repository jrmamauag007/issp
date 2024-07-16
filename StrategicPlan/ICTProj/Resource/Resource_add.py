from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def Resource_add(driver):

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    ICT = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/p[1]"))
    )
    ICT.click()

    resource = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[5]/button[1]"))
    )
    resource.click()

    add_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='flex-shrink-0 px-5 mr-8 py-2 bg-sidebar text-white rounded-2xl mt-4 ml-auto']"))
    )
    assert add_button.is_displayed(), "Add button is not visible"
    assert add_button.text == "Add New", "Add button text is incorrect"
    print(f"'Add' button is visible with text: {add_button.text}")
    add_button.click()

    # Fill out the form fields
    form_data_list = [
        {
            "number": "1"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='ICT Item']"))
                ), "ICT Item field name not found"
                print("ICT Item field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Allotment Class']"))
                ), "Allotment Class field name not found"
                print("Allotment Class field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Office']"))
                ), "Office field name not found"
                print("Office field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Proposed Number of Units to be Deployed per Year']"))
                ), "Proposed field name not found"
                print("Proposed field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Year']"))
                ), "Year field name not found"
                print("Year field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Number of Units']"))
                ), "Number field name not found"
                print("Number field name is visible")

            except AssertionError as e:
                print(e)

            item_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/div[2]/div/div/div[1]/input")
            item_field.click()
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            class_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/div[3]/div/div/div[1]/input")
            class_field.click()
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            office_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/div[4]/div/div/div[1]/input")
            office_field.click()
            time.sleep(2)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            number_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/div[5]/div[3]/div/div[2]/input")
            number_field.clear()
            number_field.send_keys(form_data["number"])

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div[2]/form/div[7]/div[2]/div/div[1]/button[2]"))
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
            expected_text = "Resource Requirements added successfully."

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
