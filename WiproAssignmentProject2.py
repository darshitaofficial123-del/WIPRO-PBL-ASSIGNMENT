# Program to suggest a mode of transport based on distance

# distance = int(input("How far would you like to travel in miles? "))

# if distance < 3:
#     print("I suggest Bicycle to your destination")
# elif distance < 300:
#     print("I suggest Motor-Cycle to your destination")
# else:
#     print("I suggest Super-Car to your destination")


# Cost of running one server

cost_per_hour = 0.51

# Cost calculations
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# Number of days with $918
days_with_918 = 918 / cost_per_day

# Display results
print("Cost to operate one server per day: $", round(cost_per_day, 2))
print("Cost to operate one server per week: $", round(cost_per_week, 2))
print("Cost to operate one server per month: $", round(cost_per_month, 2))
print("Number of days one server can operate with $918:", round(days_with_918, 2))