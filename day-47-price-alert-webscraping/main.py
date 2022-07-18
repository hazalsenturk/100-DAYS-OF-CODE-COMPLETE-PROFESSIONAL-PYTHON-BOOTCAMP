import requests
from bs4 import BeautifulSoup
import smtplib

####### GET AMAZON ALEXA PRICE ######

headers = {
    "User-Agent": "14.0.3 Safari",
    "Accept-Language": "en-us",
}

ALEXA_URL = "https://www.amazon.com/All-new-Echo-Amazon-Smart-Charcoal/dp/B08GTWC9ZB/ref=sr_1_2?crid=26J9QW3TUR2JY&dchild=1&keywords=alexa+echo+dot+4th+generation+smart+speaker+with+alexa&qid=1613945557&rnid=2941120011&s=amazon-devices&sprefix=alexa+echo+dot+4th+generation%2Caps%2C2 70&sr=1-2"
response = requests.get(ALEXA_URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
alexa_price_tag = soup.find(name="span", id="price_inside_buybox", class_="a-size-medium a-color-price").getText()
alexa_price = float(alexa_price_tag.split("$")[1])
print(alexa_price)

######## SEND EMAIL PRICE ALERT #######

EMAIL = "testpython.g21@gmail.com"
PASSWORD = "cexjyj-3cawvu-vavseH"

alexa_price=49.99
if alexa_price < 50:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: All-new Echo Dot (4th Gen) \n\n Alexa is now for {alexa_price}. "
                                                                 f"The Day Come. Hurry! \n Link: {ALEXA_URL} "
                            )