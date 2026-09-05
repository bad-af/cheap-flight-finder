from datetime import datetime

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

max_budget = ask_for_int("What is the maximum budget? (euros)")
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
