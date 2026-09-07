from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import requests
load_dotenv()
api_token = os.getenv("TRAVELPAYOUTS_TOKEN")

def ask_for_int(question):
    while True:
        try:
            answer = int(input(question))
            return answer
        except ValueError:
            print("Invalid input, try again")

def ask_for_date(question):
    while True:
        try:
            answer = datetime.strptime(input(question), "%d/%m/%Y")
            return answer
        except ValueError:
            print("Invalid date, try again")

max_budget = ask_for_int("What is the maximum budget? (euros) ")
beginning_date = ask_for_date("What is the beginning date? ")
end_date = ask_for_date("What is the end date? ")
while end_date < beginning_date:
    print("End date must be after beginning date, try again")
    end_date = ask_for_date("What is the end date? ")
min_duration = ask_for_int("What is the minimum duration? (days) ")
max_duration = ask_for_int("What is the maximum duration? (days) ")
while max_duration < min_duration:
    print("Minimum duration should be lower than maximum duration, try again")
    max_duration = ask_for_int("What is the maximum duration? (days) ")

portuguese_airports = [
    {"code": "LIS", "city": "Lisboa"},
    {"code": "OPO", "city": "Porto"},
    {"code": "FAO", "city": "Faro"},
    {"code": "FNC", "city": "Funchal"},
    {"code": "PDL", "city": "Ponta Delgada"}
]

european_destinations = [
    {"code": "MAD", "city": "Madrid"},
    {"code": "BCN", "city": "Barcelona"},
    {"code": "VLC", "city": "Valencia"},
    {"code": "SVQ", "city": "Seville"},
    {"code": "AGP", "city": "Malaga"},
    {"code": "BIO", "city": "Bilbao"},
    {"code": "CDG", "city": "Paris"},
    {"code": "BVA", "city": "Paris (Beauvais)"},
    {"code": "NCE", "city": "Nice"},
    {"code": "LTN", "city": "London (Luton)"},
    {"code": "STN", "city": "London (Stansted)"},
    {"code": "MAN", "city": "Manchester"},
    {"code": "BGY", "city": "Milan (Bergamo)"},
    {"code": "MXP", "city": "Milan (Malpensa)"},
    {"code": "FCO", "city": "Rome (Fiumicino)"},
    {"code": "CRL", "city": "Brussels (Charleroi)"},
    {"code": "BRU", "city": "Brussels (Zaventem)"},
    {"code": "DUB", "city": "Dublin"},
    {"code": "BUD", "city": "Budapest"},
    {"code": "WAW", "city": "Warsaw"},
    {"code": "BSL", "city": "Basel"},
    {"code": "ZRH", "city": "Zurich"},
    {"code": "GVA", "city": "Geneva"}
]

url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"


actual_date = beginning_date
while actual_date <= end_date:
    return_date = actual_date + timedelta(days=min_duration)
    params = {
        "token": api_token,
        "origin": "LIS",
        "destination": "MAD",
        "departure_at": actual_date.strftime("%Y-%m-%d"),
        "return_at": return_date.strftime("%Y-%m-%d"),
        "currency": "eur"
    }
    answer = requests.get(url, params=params)
    print(answer.status_code)
    print(answer.json())
    actual_date = actual_date + timedelta(days = 1)


