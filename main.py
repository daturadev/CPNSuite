#!/usr/bin/python3
# utf-8

# Imports
import sys
from colorama import Fore, Back, init
import random
import subprocess
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import os
import json
import time



# Load mappings stored in file 'data.json'
try:
    with open("data.json", "r") as file:
        state_area_mapping = json.load(file)
except FileNotFoundError:
    print(Fore.RED + "Error: data.json not found.\n")
    sys.exit(1)

# Auto-reset Colorama fonts
init(autoreset=True)

# Function to clear the console screen
def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.call(command, shell=True)

# Display homescreen
def home():
    print(Back.BLUE, Fore.WHITE + "SSN Generator and Validator")
    print(Fore.GREEN + "Usage: python main.py <state> <count>")
    print(Fore.YELLOW + "Example: python main.py CA 10")

# Validate command-line arguments
if len(sys.argv) != 3:
    print(Fore.RED + "Invalid usage. Refer to 'Usage' on homescreen...\n")
    time.sleep(2.25)
    home()
    sys.exit()

state = sys.argv[1]
count = int(sys.argv[2])
ssnlist = []

# Function to generate a random SSN based on state area
def generate_ssn(state_area):
    area_number = random.choice(state_area)
    group_number = random.randint(1, 99)
    serial_number = random.randint(1, 9999)
    return f"{area_number:03}-{group_number:02}-{serial_number:04}"

# Function to check the validity of an SSN
def check_ssn(ssn):
    url = f"https://www.ssn-verify.com/{ssn}"
    driver = uc.Chrome()
    driver.get(url)

    # Wait for the page to load
    time.sleep(random.randint(6, 11))

    try:
        # Check for validity
        result = driver.find_element(By.XPATH, "//div[@id='result']").text
    except Exception as e:
        result = f"Error fetching result: {e}"
    finally:
        driver.quit()

    return ssn, result

# Main Function
def main():
    results = []
    invalid_ssns = []
    print(Fore.YELLOW + "⚠️ Generating SSNs...\n")

    if state in state_area_mapping:
        for _ in range(count):
            ssn = generate_ssn(state_area_mapping[state])
            print(Fore.GREEN + f"Generated SSN: {ssn}")
            ssnlist.append(ssn)
            with open("SSNList.txt", "a") as file:
                file.write(ssn + "\n")

        clear_screen()
        print(Fore.GREEN + "✅ SSN list saved. Testing for validity...\n")
        time.sleep(1.75)

        for ssn in ssnlist:
            ssn, validity = check_ssn(ssn)
            results.append((ssn, validity))
            if "invalid" in validity.lower() or "not issued" in validity.lower():
                print(Fore.GREEN + "✅ Usable CPN logged!\n")
                invalid_ssns.append(ssn)
            time.sleep(random.randint(3, 12))  # Sleep for WAF Bypass

        # Print and save results
        for ssn, validity in results:
            print(Fore.YELLOW + f"SSN: {ssn}, Validity: {validity}\n")

        with open("scraped_cpns.txt", "w") as file:
            for ssn in invalid_ssns:
                file.write(f"{ssn}\n")
    else:
        print(Fore.RED + "❌ Invalid state abbreviation.")
        home()
        sys.exit()

if __name__ == "__main__":
    home()
    main()