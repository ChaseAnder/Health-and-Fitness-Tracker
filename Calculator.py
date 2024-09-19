'''
Chase Anderson
'''
import datetime

current_date = datetime.date.today()

class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{current_date}'

    def add_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f'\n{current_date}') 

class Birthday:
    def __init__(self, year, month, day ):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        birthday_str = f'{self.year}-{self.month}-{self.day}'
        return birthday_str

        

    def __str__(self):
        msg = f'{self.year}-{self.month}-{self.day}'
        return msg
    




class Steps_to_miles:
    # takes in steps and height(inches) with a default value of 0
    def __init__(self, steps = 0, height = 0):
        self.steps = steps
        self.height = (height)  # Convert height to an integer

    def get_distance(self):
        if self.height < 60:
            dist = self.steps / 2640
            return f'{dist:.2f}'
        # average stride length for someone 5'1 to 5'2 is 2.1 feet
        elif self.height > 60 and self.height < 62:
            dist = self.steps / 2514
            return f'{dist:.2f}'

        elif self.height > 61 and self.height < 65:
            dist = self.steps / 2400
            return f'{dist:.2f}'

        elif self.height > 64 and self.height < 69:
            dist = self.steps / 2296
            return f'{dist:.2f}'

        elif self.height > 68 and self.height < 72:
            dist = self.steps / 2200
            return f'{dist:.2f}'

        elif self.height > 71 and self.height < 74:
            dist = self.steps / 2112
            return f'{dist:.2f}'

        elif self.height > 73 and self.height < 77:
            dist = self.steps / 2030
            return f'{dist:.2f}'

        elif self.height > 76:
            dist = self.steps / 1956
            return f'{dist:.2f}'

    def add_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f'\tSteps: {self.steps}  Miles: {self.get_distance()}\n')

        
class Calories_burned:
    #Takes type of activity and default to unknown and takes duration(minutes) and weight(lbs) set to 0 
    def __init__(self, type_of_activity = "unknown", duration = 0, weight = 0):
        self.type_of_activity = type_of_activity
        self.duration = duration
        self.weight = weight

    def get_activityType(self):
        return self.type_of_activity
    
    #returns weight in lbs to kg
    def get_weight(self):
        return self.weight * 0.45
    
    #return duration in minutes to duration in hours
    def get_duration(self):
        self.duration = self.duration / 60
        return self.duration
    
    #takes what type of workout you made and calculates the amount of calories you burned
    def get_cals(self):
        if self.type_of_activity == "walking":
            return f'Exercise: Walk, {3.5 * self.get_duration() * self.get_weight()}'
        
        elif self.type_of_activity == "jogging":
            return f'Exercise: Jog, {7 * self.get_duration() * self.get_weight():.2f}'
        
        elif self.type_of_activity == "cycling":
            return f'Exercise: Biking, {8 * self.get_duration() * self.get_weight():.2f}'
        
        elif self.type_of_activity == "swimming":
            return f'Exercise: Swimming, {6 * self.get_duration() * self.get_weight():.2f}'
        
        elif self.type_of_activity == "weight lifting":
            return f'Exercise: Weight lifting, {6 * self.get_duration() * self.get_weight():.2f}'
        
        elif self.type_of_activity == "running":
            return f'Exercise: Run, {9.8 * self.get_duration() * self.get_weight():.2f}'
        
    def add_to_file(self,filename):
        with open(filename, 'a') as file:
            file.write(f'\tCalories burned: {self.get_cals()}, Duration: {self.duration:.2f} Hrs\n')

