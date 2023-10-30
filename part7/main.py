import requests as api
import os
import datetime as dt


GENDER = "male"
WEIGHT_KG = 67.0
HEIGHT_CM = 173.0
AGE = 32

APP_ID = os.environ["SHEETY_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_API_KEY2"]
API_KEY_SHEETY = os.environ["SHEETY_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/041bc237af12575deefd9d8f485daa6f/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
  "Content-Type": "application/json"
}

headers_sheety = {
  "Authorization": f"Bearer {API_KEY_SHEETY}",
  "Content-Type": "application/json"
}

parameters = {
  "query": exercise_text,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

def run():
  #Get information from Nutritionix API
  response = api.post(exercise_endpoint, headers=headers, json=parameters)
  response.raise_for_status()

  #Post information to Sheety API
  for exercise in response.json()["exercises"]:
    
    sheety_parameters = {
      "workout": {
      "date": dt.datetime.now().strftime("%d/%m/%Y"),
      "time": dt.datetime.now().strftime("%X"),
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
      }
    }
    
    sheety_response = api.post(sheety_endpoint, json=sheety_parameters, headers=headers_sheety)
    
    print(sheety_response.status_code)
    print(sheety_response.text)