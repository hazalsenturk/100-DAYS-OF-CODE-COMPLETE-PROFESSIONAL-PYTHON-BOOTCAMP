from selenium import webdriver
import time

chrome_drive_path = "/Users/hazalsenturk/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min_after = time.time() + 60*5
click_on = True

while click_on:

    cookie.click()

    if time.time() > timeout:
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",","")
        money_int = int(money)

        ###### BUTTONS #########
        cursor = driver.find_element_by_css_selector('#buyCursor b')
        grandma = driver.find_element_by_css_selector('#buyGrandma b')
        factory = driver.find_element_by_css_selector('#buyFactory b')
        mine = driver.find_element_by_css_selector('#buyMine b')
        shipment = driver.find_element_by_css_selector('#buyShipment b')
        alchemy_lab = driver.find_element_by_css_selector('#buyAlchemy\ lab b')
        portal = driver.find_element_by_css_selector('#buyPortal b')
        time_machine = driver.find_element_by_css_selector('#buyTime\ machine b')
        button_list = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]

        ###### PRICES #########

        cost_cursor = int(cursor.text.split("-")[1].replace(",", ""))
        cost_grandma = int(grandma.text.split("-")[1].replace(",", ""))
        cost_factory = int(factory.text.split("-")[1].replace(",", ""))
        cost_mine = int(mine.text.split("-")[1].replace(",", ""))
        cost_shipment = int(shipment.text.split("-")[1].replace(",", ""))
        cost_alchemy_lab = int(alchemy_lab.text.split("-")[1].replace(",", ""))
        cost_portal = int(portal.text.split("-")[1].replace(",", ""))
        cost_time_machine = int(time_machine.text.split("-")[1].replace(",", ""))
        price_list = [cost_cursor, cost_grandma, cost_factory, cost_mine, cost_shipment, cost_alchemy_lab, cost_portal,
                      cost_time_machine]

        affordable_support = []

        for price in price_list:
            if money_int > price:
                affordable_support.append(price)
        highest_support_possible = max(affordable_support)
        index_support = price_list.index(highest_support_possible)
        button_list[index_support].click()
        timeout = time.time() + 5

    if time.time() > five_min_after:
        cps = driver.find_element_by_id("cps").text
        print(cps)
        click_on = False


