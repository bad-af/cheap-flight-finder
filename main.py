def ask_for_int(question):
    while True:
        try:
            answer = int(input(question))
            return answer
        except ValueError:
            print("Invalid input, try again")

max_budget = ask_for_int("What is the maximum budget? ")
beggining_date = input("Beginning date? ")
end_date = input("End date? ")
min_duration = ask_for_int("What is the minimum duration? ")
max_duration = ask_for_int("What is the maximum duration? ")
print(max_budget, beggining_date, end_date, min_duration, max_duration)