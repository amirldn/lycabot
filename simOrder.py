import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Generates name
def person_generate():
    with open('./data/names.txt') as file_with_names:
        names_list = [line.rstrip() for line in file_with_names]
        first_name_in = names_list[randint(0, 4000)]
        second_name_in = names_list[randint(0, 4000)]
        email_in = str(first_name_in + second_name_in +
                      str(randint(2, 80)) + "@gmail.com")
        print(
            "Your name is " +
            first_name_in,
            second_name_in,
            "and your email is " +
            email_in)
    return first_name_in, second_name_in, email_in

# Opens website to order the sim card

driver = webdriver.Chrome()
driver.get("https://www.lycamobile.co.uk/en/order-sim/")
print("Launching Lycamobile's Site")

# Waits until the radio checkbox for "No thanks" shows up then clicks the button

elem_radio_no_bonus = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "online_retention_check_nothanks")))
print("Found no thanks checkbox")
time.sleep(2)
elem_radio_no_bonus = driver.find_element_by_id("online_retention_check_nothanks")
elem_radio_no_bonus.click()

elem_radio_terms = driver.find_element_by_id("terms_conditions")
elem_radio_terms.click()

elem_button_proceed_1 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "lyca_cart_newsim_button1")))

# Clicks proceed button

driver.execute_script("nc_newsim_open_tab1('address','fid','sid')");

first_name, last_name, email = person_generate()

elem_form_first_name = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "firstName")))

elem_form_first_name = driver.find_element_by_id("firstName")
elem_form_first_name.send_keys(first_name)

elem_form_last_name = driver.find_element_by_id("lastName")
elem_form_last_name.send_keys(last_name)

elem_form_email = driver.find_element_by_id("email")
elem_form_email.send_keys(email)

elem_radio_same_as_billing = driver.find_element_by_id("same_as_billing")
elem_radio_same_as_billing.click()







time.sleep(5)
driver.close()

