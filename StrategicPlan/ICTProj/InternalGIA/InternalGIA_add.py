from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def InternalGIA_add(driver):

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    ICT = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/p[1]"))
    )
    ICT.click()

    add_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add New']"))
    )
    assert add_button.is_displayed(), "Add button is not visible"
    assert add_button.text == "Add New", "Add button text is incorrect"
    print(f"'Save' button is visible with text: {add_button.text}")
    add_button.click()

    # Fill out the form fields
    form_data_list = [
        {
            "name": "database",
            "objectives": "objectives",
            "deliverables": "deliverables"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:
                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Name / Title of ICT Project']"))
                ), "Name field name not found"
                print("Name field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Duration']"))
                ), "Duration field name not found"
                print("Duration field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Objectives']"))
                ), "Objectives field name not found"
                print("Objectives field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Deliverables']"))
                ), "Deliverables field name not found"
                print("Deliverables field name is visible")

            except AssertionError as e:
                print(e)

            name_field = driver.find_element(By.XPATH, "//input[@id='ict_proj_name']")
            name_field.clear()
            name_field.send_keys(form_data["name"])

            # from_field = driver.find_element(By.XPATH, "//div[@class='flex-grow md:w-3\/8 relative']//div[@class='relative']//div[@class='dp__main dp__theme_light mt-2 my-1 block w-72 border-gray-400 w-full rounded-md shadow-//div//input[@value='2024']")
            # from_field.click()
            # WebDriverWait(driver, 10).until(
            #     EC.visibility_of_all_elements_located((By.CLASS_NAME, "dp__menu"))
            # )
            # # Locate the year element (e.g., 1900) and click it
            # year_element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell' and @data-test='2000']"))
            # )
            # year_element.click()
            #
            # # Locate the "Select" button and click it
            # select_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable(
            #         (By.XPATH, "//button[@class='dp__action_button dp__action_select' and @data-test='select-button']"))
            # )
            # select_button.click()

            # to_field = driver.find_element(By.XPATH, "//input[@placeholder='To']")
            # to_field.click()
            # WebDriverWait(driver, 10).until(
            #     EC.visibility_of_all_elements_located((By.CLASS_NAME, "dp__menu"))
            # )
            # # Locate the year element (e.g., 1900) and click it
            # year_element = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell' and @data-test='2000']"))
            # )
            # year_element.click()
            #
            # # Locate the "Select" button and click it
            # select_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable(
            #         (By.XPATH, "//button[@class='dp__action_button dp__action_select' and @data-test='select-button']"))
            # )
            # select_button.click()

            objectives_field = driver.find_element(By.XPATH, "//textarea[@id='ict_objectives']")
            objectives_field.clear()
            objectives_field.send_keys(form_data["objectives"])

            deliverables_field = driver.find_element(By.XPATH, "//textarea[@id='ict_deliverables']")
            deliverables_field.clear()
            deliverables_field.send_keys(form_data["deliverables"])

            # Click the save button and handle confirmation
            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[8]/button[1]"))
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
            expected_text = "Internal ICT Project added successfully."

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
