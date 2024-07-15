from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


def OS_add(driver):
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/agency-profile']"))
    )
    driver.get("http://10.10.99.23/strategic-plan")

    os = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[2]/div/ul/li[1]/p"))
    )
    os.click()

    # Fill out the form fields
    form_data_list = [
        {
            "filledmale": "1",
            "filledfemale": "1",
            "conmale": "1",
            "confemale": "1",
            "tempmale": "1",
            "tempfemale": "1",
            "source": "Externally Funded (EXT)",
            "amount": "1"
        }
    ]

    for form_data in form_data_list:
        try:
            # Assert the visibility of form fields by their placeholders
            try:

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[@class='font-bold text-black card-title mt-4 ml-5' and contains(text(),'Human Resources')]"))
                ), "Human Resources field name not found"
                print("Human Resources field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Current Annual ICT Budget']"))
                ), " Current Annual ICT Budget  field name not found"
                print(" Current Annual ICT Budget  field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Present ICT Situation (Strategic Challenges)']"))
                ), "Present ICT Situation (Strategic Challenges) field name not found"
                print("Present ICT Situation (Strategic Challenges) field name is visible")

                assert WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Strategic Concerns for ICT Use']"))
                ), "Strategic Concerns for ICT Use field name not found"
                print("Strategic Concerns for ICT Use field name is visible")


            except AssertionError as e:
                print(e)

            filledmale_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[1]/div[1]/table/tbody/tr[1]/td[2]/input")
            filledmale_field.clear()
            filledmale_field.send_keys(form_data["filledmale"])

            filledfemale_field = driver.find_element(By.XPATH, "//input[contains(@class,'female-filled-up-input border-transparent rounded text-center w-full placeholder-gray-400 placeholder-opacity-75 text-sm')]")
            filledfemale_field.clear()
            filledfemale_field.send_keys(form_data["filledfemale"])

            conmale_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[1]/div[1]/table/tbody/tr[2]/td[2]/input")
            conmale_field.clear()
            conmale_field.send_keys(form_data["conmale"])

            confemale_field = driver.find_element(By.XPATH, "//input[contains(@class,'female-contractual-input border-transparent rounded text-center w-full placeholder-gray-400 placeholder-opacity-75 text-sm')]")
            confemale_field.clear()
            confemale_field.send_keys(form_data["confemale"])

            tempmale_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/main/div/div[3]/div/form/div[1]/div[1]/table/tbody/tr[3]/td[2]/input")
            tempmale_field.clear()
            tempmale_field.send_keys(form_data["tempmale"])

            tempfemale_field = driver.find_element(By.XPATH, "//input[contains(@class,'female-non-permanent-input border-transparent rounded text-center w-full placeholder-gray-400 placeholder-opacity-75 text-sm')]")
            tempfemale_field.clear()
            tempfemale_field.send_keys(form_data["tempfemale"])

            budget_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='budget_src_fund']"))
            time.sleep(1)
            budget_dropdown.select_by_index(0)

            amount_field = driver.find_element(By.XPATH, "//input[@id='budget_amount']")
            amount_field.clear()
            amount_field.send_keys(form_data["amount"])

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
            expected_text = "Organizational Structure added successfully."

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
