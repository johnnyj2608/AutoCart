import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv

load_dotenv()
zipcode = os.getenv("ZIPCODE")
email = os.getenv("COSTCO_EMAIL")
password = os.getenv("COSTCO_PASSWORD")

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
costcoWebsite = "https://sameday.costco.com/store/account/orders"
driver.get(costcoWebsite)

try:
    zipcodeField = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-aria-:Riim6kl9:"))
    )
    zipcodeField.send_keys(zipcode)
    shopButton = WebDriverWait(driver, 10).until (
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.e-r4uysd span.e-e2f3my'))
    )
    shopButton.click()
    print('Success')
except (TimeoutException, NoSuchElementException) as e:
    print(f"Error occurred: {str(e)}")
finally:
    print('Quit')

