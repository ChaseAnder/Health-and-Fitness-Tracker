class Steps_to_miles:
    #takes in steps and height(inches) with a default value of 0
    def __init__(self, steps = 0, height = 0):
        self.steps = steps
        self.height = height

    def get_steps(self):
        return self.steps
    
    def get_height(self):
        return self.height
    
    #get_distance takes the number of steps and converts it into miles based on how tall you are
    def get_distance(self):
        if self.height < 60:
            return f'You have made a distance of {self.steps / 2640:.2f} miles'
        #average stride length for someone 5'1 to 5'2 is 2.1 feet
        elif self.height > 60 and self.height < 62:
            return f'You have made a distance of {self.steps / 2514:.2f} miles'

        elif self.height > 61 and self.height < 65:
            return f'You have made a distance of {self.steps / 2400:.2f} miles'
        
        elif self. height > 64 and  self.height < 69:
            return f'You have made a distance of {self.steps / 2296:.2f} miles'
        
        elif self.height > 68  and self.height < 72:
            return f'You have made a distance of {self.steps / 2200:.2f} miles'
        
        elif self.height > 71 and self.height < 74:
            return f'You have made a distance of {self.steps / 2112:.2f} miles'
        
        elif self.height > 73 and self.height < 77:
            return f'You have made a distance of {self.steps / 2030:.2f} miles'
        
        elif self.height > 76:
            return f'You have a distance of {self.steps / 1956:.2f} miles'
        
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
            return f'You burned {3.5 * self.get_duration() * self.get_weight()} calories during your walk'
        
        elif self.type_of_activity == "jogging":
            return f'You burned {7 * self.get_duration() * self.get_weight():.2f} calories during your jog'
        
        elif self.type_of_activity == "cycling":
            return f'You burned {8 * self.get_duration() * self.get_weight():.2f} calories during you bike ride'
        
        elif self.type_of_activity == "swimming" or self.type_of_activity == "weight lifting":
            return f'You burned {6 * self.get_duration() * self.get_weight():.2f} calories during your workout'
        
        elif self.type_of_activity == "running":
            return f'You burned {9.8 * self.get_duration() * self.get_weight():.2f} calories during your run'
        else:
            return f'Invalid input'