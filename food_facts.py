import ast
import requests

def food_facts(food):

    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query":f"{food}"}

    headers = {
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com",
        'x-rapidapi-key': "7603016162msh8263f88a5aa10dfp18e91ajsna3493aef8fcf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    dict_response = ast.literal_eval(response.text)

    # print(dict_response)

    food_facts = {
        "saturated fat": dict_response["items"][0]["fat_saturated_g"],
        "total fat": dict_response["items"][0]["fat_total_g"],
        "carbs": dict_response["items"][0]["carbohydrates_total_g"],
        "protein": dict_response["items"][0]["protein_g"],
        "sugar": dict_response["items"][0]["sugar_g"],
        "sodium": dict_response["items"][0]["sodium_mg"],
        "cholesterol": dict_response["items"][0]["cholesterol_mg"]
    }

    for key, value in food_facts.items():
        print(f"{key.title()}: {value}")