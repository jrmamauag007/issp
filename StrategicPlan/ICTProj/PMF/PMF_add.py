from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def PMF_add(driver):

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    ICT = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/p[1]"))
    )
    ICT.click()

    pmf = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[6]/button[1]"))
    )
    pmf.click()

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
            "hierarchy": "hierarchy",
            "methods": "methods",
            "responsibility": "responsibility",
            "OVI": "OVI",
            "data": "data",
            "target": "target"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Hierarchy Type']"))
                ), "Hierarchy Type field name not found"
                print("Hierarchy Type field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Hierarchy of Targeted Results']"))
                ), "Hierarchy of Targeted Results field name not found"
                print("Hierarchy of Targeted Results field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Data Collection Methods']"))
                ), "Methods field name not found"
                print("Methods field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Responsible to Collect Data']"))
                ), "Responsible to Collect Data field name not found"
                print("Responsible to Collect Data field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='OVI']"))
                ), "OVI field name not found"
                print("OVI field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Baseline Data']"))
                ), "Baseline Data field name not found"
                print("Baseline Data field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Targets']"))
                ), "Targets field name not found"
                print("Targets field name is visible")

            except AssertionError as e:
                print(e)

            item_field = driver.find_element(By.XPATH, "//input[@placeholder='Select Hierarchy Type']")
            item_field.click()
            time.sleep(1)
            options = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "vs__dropdown-menu"))
            )
            # Click the desired option (e.g., the first option)
            desired_option = options[0]  # Change the index as needed
            desired_option.click()

            hierarchy_field = driver.find_element(By.XPATH, "//textarea[@id='pmf_target']")
            hierarchy_field.clear()
            hierarchy_field.send_keys(form_data["hierarchy"])

            methods_field = driver.find_element(By.XPATH, "//textarea[@id='pmf_methods']")
            methods_field.clear()
            methods_field.send_keys(form_data["methods"])

            responsibility_field = driver.find_element(By.XPATH, "//input[@id='pmf_resp_coll_data']")
            responsibility_field.clear()
            responsibility_field.send_keys(form_data["responsibility"])

            OVI_field = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/form/div[6]/div[2]/div/div[1]/textarea")
            OVI_field.clear()
            OVI_field.send_keys(form_data["OVI"])

            data_field = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/form/div[6]/div[2]/div/div[2]/textarea")
            data_field.clear()
            data_field.send_keys(form_data["data"])

            target_field = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/form/div[6]/div[2]/div/div[3]/textarea")
            target_field.clear()
            target_field.send_keys(form_data["target"])

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/form/div[8]/button"))
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
