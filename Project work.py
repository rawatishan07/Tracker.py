# Name - Ishan Rawat
# Project - Mini Project Assignment: Daily Calorie Tracker CLI
# Date - 5th October 2025
print("Welcome to the Daily Calorie Tracker.")
# This CLI tool will help you to monitor your daily calorie intake taken in any meal.
print("Enter the Meal Name and the calories intake.")
x= int(input("Enter the number of meals you have taken today."))
Meals = []
Calories = []
for i in range(1,x+1):
    y= input("Meal Name")
    Meals.append(y)
    z= float(input("Calories intake"))
    Calories.append(z)
print("Meals taken today", Meals)
print("Calories intake", Calories)
A= sum(Calories)
print("Total Calories:", A)
Average = A/x
print("Average Calories:", Average)
Safe_Calories_Intake = 1500
Average_Safe_Calories = 600
if Average > Average_Safe_Calories :
    print("Warning!! Calories limit exceeded.")
else:
    print("Calories are normal.")
print("\n--- Meal Breakdown ---")
print(f"{'Meal Name':<20}{'Calories':>10}") 
print("-" * 30)
for meal, calorie in zip(Meals, Calories):
    print(f"{meal:<20}{calorie:>10.2f}") 
print("-" * 30)
print(f"{'TOTAL':<20}{A:>10.2f}")
q= input("Do you want to save the report to a file? (yes/no): ")
if q == 'yes':
    file_name = "calorie_report.txt"  
    with open(file_name, 'w') as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write(f"Date: 5th October 2025\n")
        file.write(f"Number of Meals: {x}\n\n")
        file.write(f"Total Calories: {A:.2f}\n")
        file.write(f"Average Calories: {Average:.2f}\n")
        Safe_Calories_Intake = 1500
        Average_Safe_Calories = 600
        if Average > Average_Safe_Calories:
            status_message = "Warning!! Calories limit exceeded.\n"
        else:
            status_message = "Calories are normal.\n"
        file.write(status_message + "\n")
        file.write("--- Meal Breakdown ---\n")
        header = f"{'Meal Name':<20}{'Calories':>10}\n"
        file.write(header)
        file.write("-" * 30 + "\n")
        for meal, calorie in zip(Meals, Calories):
            line = f"{meal:<20}{calorie:>10.2f}\n"
            file.write(line)
        file.write("-" * 30 + "\n")
        file.write(f"{'TOTAL':<20}{A:>10.2f}\n")
    print(f"\nReport successfully saved to {file_name}")
    print("Thank you for using the Daily Calorie Tracker. Stay healthy!")
else:
    print("Report not saved.")