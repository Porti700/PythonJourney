# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# https://waitbutwhy.com/2014/05/life-weeks.html
#
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until
# 90
# years old.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#  cuantos años, dias y semanas han pasado en su vida
new_age_int = int(age)
current_month = new_age_int * 12
current_weeks = new_age_int * 52
current_days = new_age_int * 365

# De los 90 años restarle los dias, años y semanas que le falta por vivir

final_months = 90*12 - current_month
final_weeks = 90*52 - current_weeks
final_days = 90*365 - current_days

print(f"You have {final_days} , {final_weeks} , and {final_months} months left.")


