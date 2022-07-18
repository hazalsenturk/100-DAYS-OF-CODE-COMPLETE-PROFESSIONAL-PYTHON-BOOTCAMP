import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 172
AGE = 27

#Sheety Auth Info

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Nutritionix API Auth Info

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
sheety_get_endpoint = os.getenv("SHEET_ENDPOINT")

headers_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

headers_sheety = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}"

}
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers_nutri)
nutritious_output = response.json()
print(nutritious_output)

today = datetime.now()
DATE = today.date().strftime("%d/%m/%Y")
TIME = today.time().strftime("%X")


for exercise in nutritious_output['exercises']:
    sheet_inputs = {
        "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": exercise['name'].title(),
        "duration": float(exercise['duration_min']),
        "calories": float(exercise['nf_calories'])
        }
    }
    sheet_response = requests.post(url=sheety_get_endpoint, json=sheet_inputs, headers=headers_sheety)
    print(sheet_response.text)



