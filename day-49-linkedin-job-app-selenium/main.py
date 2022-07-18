from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://www.linkedin.com/jobs/view/2407120452/?refId=b2a471ff-3c7f-4107-aaf9-ed3f00ae4e47")

driver.find_element_by_link_text("Sign in").click()
time.sleep(5)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("gizemhazal.senturk@gmail.com")
password.send_keys("tastamam0!")
password.send_keys(Keys.ENTER)
time.sleep(5)
# sign_in_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
# sign_in_button.click()

driver.find_element_by_css_selector('div .jobs-apply-button--top-card button ').click()
phone_number = driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2407120452,18961498,phoneNumber~nationalNumber)")
phone_number.send_keys("5385033973")
driver.find_element_by_id("ember256").click()
time.sleep(5)
driver.find_element_by_id("ember256").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2407120452,18961482,multipleChoice)"]/option[4]').click()
driver.find_element_by_xpath('//*[@id="ember263"]/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="ember265"]/div/div[1]/label').click()
driver.find_element_by_id("ember267").click()
driver.find_element_by_xpath('//*[@id="ember237"]/div/div[2]/footer/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="ember277"]').click()
