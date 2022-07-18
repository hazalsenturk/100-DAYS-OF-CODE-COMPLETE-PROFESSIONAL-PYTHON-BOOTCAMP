import requests
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_KEY = "1I6YZ6LMU2SA4POZ"

NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "2fef8829c2044e6799982608afa210a6"

MY_MAIL = "testpython.g21@gmail.com"
PASSWORD = "cexjyj-3cawvu-vavseH"

VIRTUAL_TWILIO_NUMBER = "+17735709682"
VERIFIED_NUMBER = "+905385033973"
SMS_TWILIO_TOKEN = "e8d9bc368b491da644b704e2c397957b"
SMS_TWILIO_API_SID = "AC154953f40bbab805722d298e19f6198a"

parameters_stock = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "datatype": "json",
        "apikey": ALPHA_VANTAGE_KEY
}

stock_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=parameters_stock)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_closes = [value["4. close"] for (key, value) in stock_data.items()]
two_days_closes = stock_closes[1::2]

stock_change = float(two_days_closes[1])-float(two_days_closes[0])
stock_change_percent = round((stock_change*100)/float(two_days_closes[1]))
up_down = None

if stock_change > 0:
    up_down = '🔺'
else:
    up_down = '🔻'


# TO SEND THE STOCK CHANGE AND NEWS VIA EMAIL

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_MAIL, PASSWORD)
    connection.ehlo()

    if abs(stock_change_percent) >= 1:
        parameters_news = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=parameters_news)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    print(three_articles[0]['title'])

    for article in three_articles:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Subject: NEWS"
        msg['From'] = MY_MAIL
        msg['To'] = "testpython.y21@yahoo.com"

        text = f"{STOCK}:{up_down}{stock_change_percent}%\n Headline: {article['title']}\n Brief: {article['description']}"
        html = f"""\
        <html>
          <head></head>
          <body>
            <p>{STOCK}:{up_down}{stock_change_percent}%<br>
               Headline: {article['title']}\n Brief: {article['description']}<br>
            </p>
          </body>
        </html>
        """
        part1 = MIMEText(text,'plain')
        part2 = MIMEText(html,'html')

        msg.attach(part1)
        msg.attach(part2)

        connection.sendmail(from_addr=MY_MAIL, to_addrs="testpython.y21@yahoo.com", msg=msg.as_string())


# TO SEND THE STOCK CHANGE AND NEWS VIA SMS OVER A PROVIDER AS TWILIO

# client = Client(SMS_TWILIO_API_SID, SMS_TWILIO_TOKEN)
#
# for article in three_articles:
#     message = client.messages.create(
#         body=f"Subject: NEWS \n\n {STOCK}:{stock_change_percent}%\n Headline: {article['title']}\n Brief: {article['description'].encode('utf-8')}",
#         from_=VIRTUAL_TWILIO_NUMBER,
#         to=VERIFIED_NUMBER)