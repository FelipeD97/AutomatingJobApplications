from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/Flip/Development/chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3273291833&f_AL=true&f_E=2&geoId=106224388&keywords=python%20developer&location=Atlanta%2C%20Georgia%2C%20United%20States&refresh=true&start=25"
)

sign_in = driver.find_elements(by="css selector", value="header a")[2]
# print(sign_in.text)

sign_in.click()

email = driver.find_element(by="name", value="session_key")
password = driver.find_element(by="name", value="session_password")
sign_in_button = driver.find_element(by="tag name", value="button")

email.send_keys("felipe.a.dunbar@gmail.com")
time.sleep(3)
password.send_keys("22Utopia$")
time.sleep(3)
sign_in_button.click()

# job_posting = driver.find_elements(
#     by="css selector", value=".jobs-unified-top-card__content--two-pane button"
# )
# job_id = [button.get_attribute("data-job-id") for button in job_posting][0]
# # print(job_id)
job_posting_button = driver.find_element(
    by="css selector", value=".jobs-unified-top-card__content--two-pane button"
)
# print(job_posting_button.get_attribute("data-job-id"))

job_posting_button.click()
time.sleep(3)

fnext_button = driver.find_elements(by="tag name", value="button")[1]
# buttons = [item.get_attribute("aria-label") for item in fnext_button]
next_button_label = fnext_button.get_attribute("aria-label")
fnext_button.click()

# fnext_button = driver.find_elements(by="aria-", value="button")[1]
# fnext_button.click()


# driver.close()
