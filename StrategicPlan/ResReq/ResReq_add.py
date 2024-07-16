from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def ResReq_add(driver):

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/strategic-plan']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    resreq = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/p[1]"))
    )
    resreq.click()

    try:
        # Assert the visibility of form fields by their placeholders
        try:
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'font-bold text-black card-title mt-5 ml-5') and contains(text(), 'ICT ORGANIZATIONAL STRUCTURE')]"))
            ), "ICT ORGANIZATIONAL STRUCTURE field name not found"
            print("ICT ORGANIZATIONAL STRUCTURE field name is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Existing ICT Organizational Structure']"))
            ), "Existing ICT Organizational Structure field name not found"
            print("Existing ICT Organizational Structure field name is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[2]/div/div/button"))
            ), "Browse button not found"
            print("Browse button is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Proposed ICT Organizational Structure']"))
            ), "Proposed ICT Organizational Structure field name not found"
            print("Proposed ICT Organizational Structure field name is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[2]/div/div/button"))
            ), "Browse button not found"
            print("Browse button is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'Placement of the Proposed ICT Organizational Structure in the Agency Organizational Structure')]"))
            ), "Placement of the Proposed ICT Organizational Structure in the Agency Organizational Structure  field name not found"
            print("Placement of the Proposed ICT Organizational Structure in the Agency Organizational Structure  field name is visible")

            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[3]/div/div/button"))
            ), "Browse button not found"
            print("Browse button is visible")

        except AssertionError as e:
            print(e)

        existing_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[1]/div/input")
        existing_field.send_keys('C:/Users/jrmam/test/pythonProject/StrategicPlan/img.png')

        proposed_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[2]/div/input")
        proposed_field.send_keys('C:/Users/jrmam/test/pythonProject/StrategicPlan/img.png')

        placement_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[2]/div/div[3]/div/input")
        placement_field.send_keys('C:/Users/jrmam/test/pythonProject/StrategicPlan/img.png')


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
        expected_text = "Successfully Saved ICT Organizational Structure."

        if actual_text == expected_text:
            # Find and click the OK button
            ok_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
            )
            assert ok_button.is_displayed(), "OK button is not visible"
            assert ok_button.text == "OK", "OK button text is incorrect"
            print(f"'OK' button is visible with text: {ok_button.text}")
            ok_button.click()
            print(f"Input success")
        else:
            print(f"Input failed")
            raise Exception(f"Unexpected success message: {actual_text}")
            # Handle the exception (e.g., if success message not found)
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
