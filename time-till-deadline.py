import datetime

user_input = input("Enter your goal with a deadline, separate it by colon: \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.datetime.today()

time_calculated = deadline_date - current_date
print(f"Time remaining for your goal: {time_calculated.days}")
