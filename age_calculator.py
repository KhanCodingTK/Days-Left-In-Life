age = input("What is your current age? ")

age_as_int = int(age)
years_remaning = (90 - age_as_int)
days_left = 365*years_remaning
weeks_left = 52*years_remaning
months_left = 12*years_remaning

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


