import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from func import *

def detect_elem(elem_id):
    detected_elem = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, elem_id))
    )
    return detected_elem

def add_sim():
    detect_elem("siminc").click()
    print("SIM Added")
    time.sleep(7)
    # no_of_sims = WebDriverWait(driver,50).until(
    #     EC.text_to_be_present_in_element(By.ID,"simcount"))


def from_terms_to_entry():
    elem_radio_no_bonus = driver.find_element_by_id("online_retention_check_nothanks")
    elem_radio_no_bonus.click()

    elem_radio_terms = driver.find_element_by_id("terms_conditions")
    elem_radio_terms.click()

    # Clicks proceed button
    elem_button_proceed_1 = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "lyca_cart_newsim_button1"))
    )
    driver.execute_script("nc_newsim_open_tab1('address','fid','sid')")

    elem_form_first_name = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.ID, "firstName"))
    )

    print("Formloaded")

    elem_form_first_name = driver.find_element_by_id("firstName")
    # elem_form_first_name.send_keys(first_name)
    for letter in first_name:
        time.sleep(randint(0, 1))  # sleep between 0 and 1 seconds
        elem_form_first_name.send_keys(letter)

    time.sleep(randint(1, 3))

    elem_form_last_name = driver.find_element_by_id("lastName")
    for letter in last_name:
        time.sleep(randint(0, 1))
        elem_form_last_name.send_keys(letter)
    # elem_form_last_name.send_keys(last_name)

    time.sleep(randint(1, 3))

    elem_form_email = driver.find_element_by_id("email")
    for letter in email:
        time.sleep(randint(0, 1))
        elem_form_email.send_keys(letter)
    # elem_form_email.send_keys(email)

    time.sleep(randint(1, 3))

    elem_form_post = driver.find_element_by_id("postCodes")
    elem_form_post.send_keys(postcode_in)

    time.sleep(1)
    driver.execute_script("findAddress()")

    print("Finding Address")
    time.sleep(
        3
    )  # Improve this by not waiting time and instead detecting when it appears on the page

    elem_dropdown_addy_list = driver.find_element(By.ID, "select-country-selectized")
    elem_dropdown_addy_list.click()

    elem_form_address = driver.find_element(By.ID, "select-country-selectized")
    elem_form_address.send_keys(door_number + Keys.ENTER)

    elem_radio_same_as_billing = driver.find_element_by_id("same_as_billing")
    elem_radio_same_as_billing.click()

    # Remove captcha
    elem_captcha = driver.find_element_by_id("free_sim_captcha")
    driver.execute_script(
        """
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """,
        elem_captcha,
    )

    # Submit
    print("Sleeping for 10 to prevent bot protection")
    time.sleep(10)

    try:
        detect_elem("lyca_cart_newsim_button1").click()
        # elem_button_proceed_2.click()
    except:
        print("Proceed button not found, falling back to submitting JS")
        driver.execute_script("nc_newsim_open_tab2('payment','sid','tid')")

    time.sleep(10)

    if driver.current_url == "https://www.lycamobile.co.uk/en/success-freesim/":
        print("SIM Ordered successfully! Closing in 5 seconds...")
        time.sleep(5)
        driver.close()
        quit(0)
    else:
        print("The site detected you were a bot, running again!")
        time.sleep(5)
        add_sim()
        from_terms_to_entry()









# Address Info
postcode_in, door_number = address()

# Generates name
first_name, last_name, email = person_generate()

# Opens website to order the sim card
driver = webdriver.Chrome()
driver.get("https://www.lycamobile.co.uk/en/order-sim/")
print("Launching Lycamobile's Site")

# Waits until the radio checkbox for "No thanks" shows up then clicks the button
detect_elem("online_retention_check_nothanks")
print("Site loaded")
time.sleep(2)
from_terms_to_entry()


# try:
#     elem_valid_order = WebDriverWait(driver, 50).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "hello-my-plan-content")))
#     print("SIM Ordered successfully! Closing in 5 seconds...")
#     time.sleep(5)
#     driver.close()
# except:
#     print("Something went wrong... Please try again")
#     time.sleep(10)
#     # driver.close()


