import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_amazon(email, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    with webdriver.Chrome(options=options) as driver:
        driver.get('https://www.amazon.com/ap/signin')
        wait = WebDriverWait(driver, 10)

        email_field = wait.until(EC.presence_of_element_located((By.ID, 'ap_email')))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        password_field = wait.until(EC.presence_of_element_located((By.ID, 'ap_password')))
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # wait for the page to load by checking if sign-out link is present
        try:
            wait.until(EC.presence_of_element_located((By.ID, 'nav-item-signout')))
            print('Login successful.')
        except Exception:
            print('Login may have failed. Please check your credentials or complete any additional verification steps.')


def main():
    email = os.getenv('AMAZON_EMAIL')
    password = os.getenv('AMAZON_PASSWORD')

    if not email or not password:
        raise ValueError('Set AMAZON_EMAIL and AMAZON_PASSWORD environment variables.')

    login_amazon(email, password)


if __name__ == '__main__':
    main()
