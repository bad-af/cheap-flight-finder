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

max_budget = ask_for_int("What is the maximum budget? ")
beggining_date = ask_for_date("What is the beggining date? ")
end_date = ask_for_date("What is the end date? ")
while end_date < beggining_date:
    print("End date must be after beginning date, try again")
    end_date = ask_for_date("What is the end date? ")
min_duration = ask_for_int("What is the minimum duration? ")
max_duration = ask_for_int("What is the maximum duration? ")
