# Name: [Jitesh Kumar]
# Roll no: 2501010180
# Date: 25 Oct 2025
# Project: Daily Calorie Tracker 


print("\t\t\tWelcome to the Daily Calorie Tracker!")

meal_names = []
calorie_values = []

num_meals = int(input("\nHow many meals do you want to enter today? "))

for i in range(num_meals):
    print("\nMeal", i+1)  # Shows Meal 1, Meal 2, etc.
    meal = input("Enter meal name: ")
    calories = float(input(" Enter calories: "))  # space added before prompt
    meal_names.append(meal)
    calorie_values.append(calories)

total_calories = sum(calorie_values)
average_calories = total_calories / num_meals
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status = "Warning! You have exceeded your daily calorie limit."
else:
    status = "Great! You are within your daily calorie limit."

print("\nYour Daily Calorie Summary:")
print("Meal Name\tCalories")
print("-------------------------")
for i in range(num_meals):
    print(meal_names[i], "\t\t", calorie_values[i])
print("-------------------------")
print("Total:\t\t", total_calories)
print("Average:\t", average_calories)
print(status)
