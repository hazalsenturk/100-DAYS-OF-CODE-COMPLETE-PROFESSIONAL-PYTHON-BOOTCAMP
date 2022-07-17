from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

############  GET LISTING INFORMATION BY ZILLOW #####################

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
    "Accept-Language": "en-US"
}

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

response = requests.get(ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


links = [link.get("href") for link in soup.find_all(name="a", class_="list-card-link", tabindex="0")]
index = 0
while index < len(links):
    if "http" not in links[index]:
        links[index] = f"https://www.zillow.com{links[index]}"
    index += 1
prices = [price.text for price in soup.find_all(name="div", class_="list-card-price")]
addresses = [address.text for address in soup.find_all(name="address", class_="list-card-addr")]


############  FILL OUT GOOGLE FORMS BY SELENIUM #####################

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeq56rUl48Ahah8ZnjdnaCfCPjkj18Mo567PrEyaxUa6SlV_A/viewform?usp=sf_link"

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get(FORM_URL)
time.sleep(2)

for i in range(0, len(addresses)):
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[i])
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()
    time.sleep(2)

    add_answer = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(2)




