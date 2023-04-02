import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
profile = r"C:\Users\hp\AppData\Local\Google\Chrome\User Data\Profile 1"
options.add_argument(f"user-data-dir={profile}")
# Use the undetected_chromedriver library to create a new driver instance
with webdriver.Chrome(options=options) as driver:
    # Maximize browser
    driver.maximize_window()

    # Launch URL
    driver.get("https://www.youtube.com/")
    print("Opened YouTube")

    # Wait for profile icon to be clickable
    profile_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#avatar-btn'))
    )

    # Click the profile icon to open the account menu
    profile_icon.click()
    print("Clicked profile icon")

    # Wait for the switch button to be visible
    switch_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#items > ytd-compact-link-renderer:nth-child(3)'))
    )

    # Click the switch button to switch to a different account
    switch_button[0].click()
    print("Clicked switch button")

    # Wait for the new profile to be visible
    newprofile = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#contents > ytd-account-item-renderer:nth-child(1)'))
    )

    # Click the new profile to select it
    newprofile[0].click()
    print("Selected new profile")

    input("press enter to quit")
