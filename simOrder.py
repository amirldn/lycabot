import time
import re
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def address():
    user_postcode = str(
        input("What's the postcode of the address you'd like to send to? "))
    user_postcode = user_postcode.upper()
    while True:
        if re.findall("[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}", user_postcode):
            postcode_data_input = user_postcode
            door_number = str(input("Door Number? "))
            break
        else:
            print("Not a valid choice")
            user_postcode = input(
                "What's the postcode of the address you'd like to send to? ")

    return postcode_data_input, door_number


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

# Address Info
postcode_in, door_number = address()

# Generates name
first_name, last_name, email = person_generate()


# Opens website to order the sim card

driver = webdriver.Chrome()
driver.get("https://www.lycamobile.co.uk/en/order-sim/")
print("Launching Lycamobile's Site")

# Waits until the radio checkbox for "No thanks" shows up then clicks the button

elem_radio_no_bonus = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "online_retention_check_nothanks")))
print("Site loaded")
time.sleep(2)
elem_radio_no_bonus = driver.find_element_by_id("online_retention_check_nothanks")
elem_radio_no_bonus.click()

elem_radio_terms = driver.find_element_by_id("terms_conditions")
elem_radio_terms.click()

elem_button_proceed_1 = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.ID, "lyca_cart_newsim_button1")))

# Clicks proceed button

driver.execute_script("nc_newsim_open_tab1('address','fid','sid')")



elem_form_first_name = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.ID, "firstName")))

elem_form_first_name = driver.find_element_by_id("firstName")
# elem_form_first_name.send_keys(first_name)
for letter in first_name:
    time.sleep(random.randint(0, 1))  # sleep between 1 and 3 seconds
    elem_form_first_name.send_keys(letter)

time.sleep(randint(1,3))


elem_form_last_name = driver.find_element_by_id("lastName")
elem_form_last_name.send_keys(last_name)
time.sleep(randint(1,3))

elem_form_email = driver.find_element_by_id("email")
elem_form_email.send_keys(email)


elem_form_post = driver.find_element_by_id("postCodes")
elem_form_post.send_keys(postcode_in)

time.sleep(1)
driver.execute_script("findAddress()")


print("Finding Address")
time.sleep(3) # Improve this by not waiting time and instead detecting when it appears on the page

elem_dropdown_addy_list = driver.find_element(By.ID, 'select-country-selectized')
elem_dropdown_addy_list.click()

elem_form_address = driver.find_element(By.ID, "select-country-selectized")
elem_form_address.send_keys(door_number + Keys.ENTER)

# elem_radio_same_as_billing = driver.find_element_by_id("same_as_billing")
# elem_radio_same_as_billing.click()

# Remove captcha
elem_captcha = driver.find_element_by_id('free_sim_captcha')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", elem_captcha)

# Submit
print("Sleeping for 20 to prevent bot protection")
time.sleep(20)
elem_button_proceed_2 = driver.find_element_by_id("lyca_cart_newsim_button1")
elem_button_proceed_2.click()

# driver.execute_script("nc_newsim_open_tab2('payment','sid','tid')")

try:
    elem_valid_order = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, "hello-my-plan-content")))
    print("VALID ORDER")
    time.sleep(5)
    driver.close()
except:
    print("Something went wrong... Please try again")
    time.sleep(10)
    driver.close()


time.sleep(10)
driver.close()

