'''
Chase Anderson
Wrote files.py
'''
from Calculator import Date
from Calculator import Steps_to_miles
from Calculator import Calories_burned
from Calorie_goal_calculator import CalorieCalculator
from datetime import datetime
'''
Ayo Taki
wrote SleepTracker class
'''
class SleepTracker:
    def __init__(self):
        self.sleep_log = []

    def record_sleep(self, start_time, end_time, quality):
        self.sleep_log.append({
            'start_time': start_time,
            'end_time': end_time,
            'quality': quality
        })

    def get_total_sleep(self):
        total_sleep = 0
        for sleep_entry in self.sleep_log:
            start_time = sleep_entry['start_time']
            end_time = sleep_entry['end_time']
            duration = (end_time - start_time).total_seconds() / 3600  # Convert to hours
            total_sleep += duration
        return total_sleep

    def get_average_quality(self):
        total_quality = 0
        num_entries = len(self.sleep_log)
        if num_entries == 0:
            return 0
        for sleep_entry in self.sleep_log:
            total_quality += sleep_entry['quality']
        return total_quality / num_entries

    def add_to_file(self, filename):
        with open(filename, 'a') as file:
            for sleep_entry in self.sleep_log:
                start_time = sleep_entry['start_time'].strftime("%Y-%m-%d %H:%M")
                end_time = sleep_entry['end_time'].strftime("%Y-%m-%d %H:%M")
                quality = sleep_entry['quality']
                file.write(f'\tSleep: Start Time: {start_time}, End Time: {end_time}, Quality: {quality}\n')
            
            total_sleep_hours = self.get_total_sleep()
            file.write(f'Total Sleep Hours: {total_sleep_hours:.2f}\n')

current_date = datetime.now().date()  # Get the current date
date = Date(current_date)
#Creates the file if one is not made already
filename = "Fitness_and_Health_Tracker.txt"
file = open(filename, 'a')
file.close()
file = open(filename, 'r')
lines = file.readlines()

# Get user information and write it to the file if not already present
if not lines:
    with open(filename, 'w') as file:
        get_birthday = input("Enter your birthday (YYYY-MM-DD) -> ")
        height = int(input("Enter height in inches -> "))
        weight = int(input("Enter weight in lbs -> "))
        file.write(f'Birthday: {get_birthday}\tHeight: {height} inches\t Weight: {weight} lbs\n')

    # Calculate age from your birthday
    birth_year = int(get_birthday.split('-')[0])
    birth_month = int(get_birthday.split('-')[1])
    birth_day = int(get_birthday.split('-')[2])
    age = current_date.year - birth_year - ((current_date.month, current_date.day) < (birth_month, birth_day))
    
    # Prompt user for fitness goal and write to file
    gender = input("Enter your gender (male/ female) -> ").lower()
    goal = input('What is your goal (gain, lose, or maintain) weight -> ').lower()
    cals_calculator = CalorieCalculator(age, weight, height, gender, goal)
    with open(filename, 'a') as add:
        add.write(f"Fitness Goal: {goal}  Recommended Cals/Day: {cals_calculator.daily_calorie_goal()}\n")

while True:
    #user interface that allows you to pick what you want to record
    user_interface = input("User Interface\nWhat would you like to add? (steps, workout, sleep, or quit) -> ").lower()

    if user_interface == 'steps':
        steps = int(input("Enter your steps -> "))
        steps_miles = Steps_to_miles(steps, height)
        date.add_to_file(filename)
        steps_miles.add_to_file(filename)
    elif user_interface == 'workout':
        type_of_activity = input("Enter (walking, jogging, cycling, weight lifting, swimming, running, or none) -> ").lower()
        if type_of_activity != 'none':
            duration = int(input("Enter duration of your workout in minutes -> "))
            calories_burned = Calories_burned(type_of_activity, duration, weight)
            date.add_to_file(filename)
            calories_burned.add_to_file(filename)
    # Ayo Taki also wrote the sleep option
    elif user_interface == "sleep":
        print("Welcome to Sleep Tracker!")
        tracker = SleepTracker()
        while True:
            print("\nOptions:")
            print("1. Record Sleep")
            print("2. Quit")

            choice = input("Enter your choice (1 or 2): ")

            if choice == '1':
                print("\nEnter Sleep Information:")
                start_time = datetime.strptime(input("Start Time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                end_time = datetime.strptime(input("End Time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                quality = float(input("Sleep Quality (1-10): "))
                date.add_to_file(filename)
                tracker.record_sleep(start_time, end_time, quality)
                print("Sleep recorded successfully!")
                tracker.add_to_file(filename)
                print("Sleep information written to file.")
                break

            elif choice == '2':
                print("Exiting Sleep Tracker. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
    #Ends while loop 
    elif user_interface == 'quit':
        break
# prints a suprise on your birthday 
if lines and lines[0][15:20] == current_date.strftime("%m-%d"):
    print("\t\t*\n\t\t|\n\t\t|\n\t <_____________>\n\t |    Happy    |\n\t |\tB      |\n\t |\tD      |\n\t |\tA      |\n\t |\tY      |\n\t |     !!!     |\n\t^---------------^\n")
