from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"
similar_account = "chloe_t"
USERNAME = "yaprak.smhgl"
PASSWORD = "helloworld2021"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        name = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        key = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        name.send_keys(USERNAME)
        key.send_keys(PASSWORD)
        key.send_keys(Keys.ENTER)

    def skip_save(self):
        not_now = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()

    def notification_turn_off(self):
        not_now = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now.click()

    def find_followers(self, fav_account):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(fav_account)
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()

    # def follow(self):
    #     self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    #     for i in range(1, 11):
    #         path = f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button'
    #         button = self.driver.find_element_by_xpath(path)
    #         time.sleep(1)
    #         button.click()
    #         time.sleep(1)

    def follow(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower()
insta_bot.login()
time.sleep(5)
insta_bot.skip_save()
time.sleep(5)
insta_bot.notification_turn_off()
time.sleep(5)
insta_bot.find_followers(similar_account)
time.sleep(5)
insta_bot.follow()
