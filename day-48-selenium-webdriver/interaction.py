from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_drive_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# statistics = driver.find_element_by_css_selector("#articlecount a").text
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Hazal")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Senturk")
mail = driver.find_element_by_name("email")
mail.send_keys("gizemhazal.senturk@gmail.com")
sign_up_click = driver.find_element_by_xpath("/html/body/form/button")
sign_up_click.click()
