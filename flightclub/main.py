import requests

SHEET_ENDPOINT = "https://api.sheety.co/46ac13bd59243d8f140dcf4da4ef2813/flightdeals/users"

print("Welcome to Hazal's Flight Club. \nWe find the bes flight deals and email you.")

name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
check_email = input("Type your email again:\n")

if email==check_email:
  
  print("You're in the club!")

  user_info = {
    "user": {
      "First Name": name,
      "Last Name": last_name,
      "Email": email
    }
  }
  response = requests.post(url=SHEET_ENDPOINT, json=user_info)
