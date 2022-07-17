# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib

TWILIO_SID = "AC154953f40bbab805722d298e19f6198a"
AUTH_TOKEN = "e8d9bc368b491da644b704e2c397957b"
VIRTUAL_NUMBER = "+17735709682"
MY_NUMBER = "+905385033973"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "testpython.g21@gmail.com"
MY_PASSWORD = "cexjyj-3cawvu-vavseH"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_NUMBER,
            to=MY_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
