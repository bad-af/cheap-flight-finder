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

best_per_route = {}
for origin in portuguese_airports:
    for destination in european_destinations:
        actual_date = beginning_date
        while actual_date <= end_date:
            return_date = actual_date + timedelta(days=min_duration)
            params = {
                "token": api_token,
                "origin": origin["code"],
                "destination": destination["code"],
                "departure_at": actual_date.strftime("%Y-%m-%d"),
                "return_at": return_date.strftime("%Y-%m-%d"),
                "currency": "eur"
            }
            answer = requests.get(url, params=params)
            flights = answer.json()["data"]
            if flights:
                cheapest_flight = flights[0]
                cheapest_price = cheapest_flight["price"]
                if cheapest_price <= max_budget:
                    route_key = origin["city"] + "-" + destination["city"]
                    new_result = {
                        "origin": origin["city"],
                        "destination": destination["city"],
                        "departure date" : actual_date,
                        "return date" : return_date,
                        "price" : cheapest_price,
                        "airline" : cheapest_flight["airline"],
                        }
                    if route_key not in best_per_route:
                        best_per_route[route_key] = new_result
                    else:
                        if new_result["price"] < best_per_route[route_key]["price"]:
                            best_per_route[route_key] = new_result

            actual_date = actual_date + timedelta(days = 1)

sorted_results = sorted(best_per_route.values(), key=lambda item: item["price"])
for result in sorted_results:
    print(f"{result["origin"]} -> {result["destination"]}")
    print(f"{result["price"]} euros go and back")
    print(f"{result["departure date"].strftime("%d/%m")} -> {result["return date"].strftime("%d/%m")}")
    print(f"airline: {result["airline"]}")


