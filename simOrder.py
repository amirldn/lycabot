import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from func import *
import undetected_chromedriver as uc


def detect_elem(elem_id):
    detected_elem = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, elem_id))
    )
    return detected_elem


def add_sim():
    detect_elem("siminc").click()
    print("SIM Added")
    time.sleep(5)
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

    print("Form loaded - entering address")
    elem_form_first_name = driver.find_element_by_id("firstName")
    elem_form_first_name.send_keys(first_name)
    elem_form_last_name = driver.find_element_by_id("lastName")
    elem_form_last_name.send_keys(last_name)
    elem_form_email = driver.find_element_by_id("email")
    elem_form_email.send_keys(email)
    elem_form_post = driver.find_element_by_id("postCodes")
    elem_form_post.send_keys(postcode_in)
    driver.execute_script("findAddress()")

    # TODO: Improve this by not waiting time and instead detecting when it appears on the page
    print("Finding Address")
    time.sleep(
        3
    )

    elem_dropdown_addy_list = driver.find_element(By.ID, "select-country-selectized")
    elem_dropdown_addy_list.click()

    elem_form_address = driver.find_element(By.ID, "select-country-selectized")
    elem_form_address.send_keys(door_number + Keys.ENTER)

    elem_radio_same_as_billing = driver.find_element_by_id("same_as_billing")
    elem_radio_same_as_billing.click()

    # Bypass captcha
    elem_captcha = driver.find_element_by_id("free_sim_captcha")
    driver.execute_script(
        """
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """,
        elem_captcha,
    )

    # Submit
    print("Sleeping for 3 secs to prevent bot protection")
    time.sleep(3)
    driver.execute_script("nc_newsim_open_tab2('payment','sid','tid')")

    time.sleep(10)

    if "success freesim" in driver.title:
        print("SIM Ordered successfully! Closing in 5 seconds...")
        time.sleep(5)
        driver.close()
        quit(0)
    else:
        print("An error occurred, running again!")
        time.sleep(2)
        for i in range(no_of_sims):
            add_sim()
        from_terms_to_entry()


# Asks for number of sims
no_of_sims = 3

# Address Info
postcode_in, door_number = address()

# Generates name
first_name, last_name, email = person_generate()

# Opens website to order the sim card
options = uc.ChromeOptions()
options.headless = True
options.add_argument('--headless')
# driver = uc.Chrome(options=options)
driver = uc.Chrome()
driver.get("https://www.lycamobile.co.uk/en/order-sim/")
print("Launching Lycamobile's Site")

# Waits until the radio checkbox for "No thanks" shows up then clicks the button
detect_elem("online_retention_check_nothanks")
print("Site loaded: %s" % driver.title)
time.sleep(2)
for i in range(no_of_sims):
    add_sim()
from_terms_to_entry()
