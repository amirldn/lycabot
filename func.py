import re
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Asks for and validates the address
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
            "Full Name: " +
            first_name_in,
            second_name_in,
            "\nEmail: " +
            email_in)
    return first_name_in, second_name_in, email_in

def num_of_sims_to_order():
    while True:
        num = input("How many SIMs would you like? ")
        try:
            if int(num) <= 3 and int(num) >= 1:
                break
            else:
                print("Please insert a number between 1 and 3")
        except:
            print("Please insert a number between 1 and 3")
    return int(num)