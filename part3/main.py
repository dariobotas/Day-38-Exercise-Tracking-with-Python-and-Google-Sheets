import requests as api
import os


GENDER = "male"
WEIGHT_KG = 67.0
HEIGHT_CM = 173.0
AGE = 32

APP_ID = "e0cbfc20"
API_KEY = os.environ["NUTRITIONIX_API_KEY2"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type":"application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

def run():
  response = api.post(exercise_endpoint, headers=headers, json=parameters)
  response.raise_for_status()
  print(response.json())