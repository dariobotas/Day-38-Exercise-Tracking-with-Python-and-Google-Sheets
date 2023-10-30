import requests as api
import os
import datetime as dt


GENDER = "male"
WEIGHT_KG = 67.0
HEIGHT_CM = 173.0
AGE = 32

APP_ID = "e0cbfc20"
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
  "Authorization": f"Bearer {API_KEY_SHEETY}",#.format(API_KEY_SHEETY),
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
  response = api.post(exercise_endpoint, headers=headers, json=parameters)
  response.raise_for_status()
  #print(response.json())
  """response = {
    'exercises': [{
      'tag_id': 317,
      'user_input': 'ran',
      'duration_min': 31.08,
      'met': 9.8,
      'nf_calories': 340.12,
      'photo': {
        'highres':
        'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
        'thumb':
        'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
        'is_user_uploaded': False
      },
      'compendium_code': 12050,
      'name': 'running',
      'description': None,
      'benefits': None
    }, {
      'tag_id': 5,
      'user_input': 'cycling',
      'duration_min': 30,
      'met': 10,
      'nf_calories': 335,
      'photo': {
        'highres':
        'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_highres.jpg',
        'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_thumb.jpg',
        'is_user_uploaded': False
      },
      'compendium_code': 1040,
      'name': 'road cycling',
      'description': None,
      'benefits': None
    }]
  }"""
  #Get now date - from datetime module
  #Get now hour - from datetime module
  #Get 'name' field (of exercise)
  #get 'duration_min' field
  #get 'nf_calories' field
  #print(response)
  #exercise_list = [
  #  (exercise['name'], exercise['duration_min'], exercise['nf_calories'])
  #  for exercise in response["exercises"]
  #]
  #print(exercise_list)

  for exercise in response.json()["exercises"]:#exercise_list:
    #print(exercise)
    sheety_parameters = {
      "workout": {
      "date": dt.datetime.now().strftime("%d/%m/%Y"),#"25/10/2023",
      "time": dt.datetime.now().strftime("%X"),#"15:00:00",
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
      }
    }
    #print(sheety_parameters)
    sheety_response = api.post(sheety_endpoint, json=sheety_parameters, headers=headers_sheety)
    #sheety_response.raise_for_status()
    print(sheety_response.status_code)
    print(sheety_response.text)
#  sheety_response = api.get(sheety_endpoint, headers=headers_sheety)
#  sheety_response.raise_for_status()
#  print(sheety_response.json())
