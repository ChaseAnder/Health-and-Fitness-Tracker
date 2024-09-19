'''
Ayo Taki
'''
from datetime import datetime

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

def get_datetime_from_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            return date_time
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD HH:MM.")

def main():
    print("Welcome to Sleep Tracker!")
    tracker = SleepTracker()

    while True:
        print("\nOptions:")
        print("1. Record Sleep")
        print("2. Show Sleep Stats")
        print("3. Quit")

        choice = input("Enter your choice (1,2, or 3): ")

        if choice == '1':
            print("\nEnter Sleep Information:")
            start_time = get_datetime_from_input("Start Time (YYYY-MM-DD HH:MM): ")
            end_time = get_datetime_from_input("End Time (YYYY-MM-DD HH:MM): ")
            quality = float(input("Sleep Quality (1-10): "))
            tracker.record_sleep(start_time, end_time, quality)
            print("Sleep recorded successfully!")

        elif choice == '2':
            total_sleep_hours = tracker.get_total_sleep()
            average_quality = tracker.get_average_quality()
            print(f"Sleep: {total_sleep_hours:.2f}")
            print(f"Average Sleep Quality: {average_quality:.2f}")

        elif choice == '3':
            print("Exiting Sleep Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    main()
