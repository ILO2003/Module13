from helper import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("enter a number and and conversion unit:\n")
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dictionary)
    validate_and_execute(days_and_units_dictionary)
