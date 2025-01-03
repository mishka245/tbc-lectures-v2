# Will not work if verification or MFA is required to log in

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Gmail credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
RECIPIENT = "recipient_email@gmail.com"
SUBJECT = "Automated Email from Selenium"
BODY = "Hello,\n\nThis is a test email sent using Selenium.\n\nBest regards,\nYour Bot"
ATTACHMENT_PATH = "/path/to/your/file.txt"  # Provide a valid file path

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure you have the correct WebDriver installed
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open Gmail
    driver.get("https://mail.google.com/")
    print("Opened Gmail")

    # Step 2: Log in
    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Wait for password input to load
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    print("Logged in to Gmail")

    # Step 3: Compose an email
    compose_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I.T-I-KE.L3")))
    compose_button.click()

    to_input = wait.until(EC.presence_of_element_located((By.NAME, "to")))
    to_input.send_keys(RECIPIENT)

    subject_input = driver.find_element(By.NAME, "subjectbox")
    subject_input.send_keys(SUBJECT)

    body_input = driver.find_element(By.CSS_SELECTOR, ".Am.Al.editable.LW-avf")
    body_input.send_keys(BODY)

    # Step 4: Add attachment (optional)
    if ATTACHMENT_PATH and os.path.exists(ATTACHMENT_PATH):
        attachment_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        attachment_input.send_keys(ATTACHMENT_PATH)
        print("Attached file")

    # Step 5: Send the email
    send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")))
    send_button.click()

    print("Email sent successfully!")

finally:
    # Step 6: Close the browser
    time.sleep(5)  # Allow some time to observe the process
    driver.quit()
    print("Browser closed")