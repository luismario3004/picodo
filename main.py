from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from uuid import uuid4
import time
import faker

fake = faker.Faker()

def generate_random_email():
    return fake.email()

def generate_random_password():
    return f"@Pentionr{str(uuid4().int)[:3]}W"

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

while True:
    try:
        email = generate_random_email()
        password = generate_random_password()

        driver.get('https://my.picodi.com/ph/refer/9b3dd447-79f5-46cf-a335-41e1851f8fe3')

        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        confirm_password_field = driver.find_element(By.NAME, 'confirm_password')
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)

        submit_button.click()

        time.sleep(5)  # Wait for page to load or redirect

        print(f"Signed up with email: {email} and password: {password}")
    except Exception as e:
        print(f"Error during signup: {e}")
    time.sleep(2)  # Add a delay between attempts

driver.quit()
