from selenium import webdriver

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_drive_path)

# driver.get("https://www.amazon.com/All-new-Echo-Amazon-Smart-Charcoal/dp/B08GTWC9ZB/ref=sr_1_2?crid=26J9QW3TUR2JY&dchild=1&keywords=alexa+echo+dot+4th+generation+smart+speaker+with+alexa&qid=1613945557&rnid=2941120011&s=amazon-devices&sprefix=alexa+echo+dot+4th+generation%2Caps%2C2 70&sr=1-2" )
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)

driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

#driver.close()
driver.quit()

