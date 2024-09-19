'''
kanaan gute
'''
class CalorieCalculator:
	def __init__(self, age = 0, weight = 0, height = 0, gender = "Not Given", goal = "None"):
		self.age = age
		self.weight = weight
		self.height = height
		self.gender = gender.lower()
		self.goal = goal.lower()
	
	def calculate_bmr(self):
		if self.gender == 'male':
			bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age) + 6
		elif self.gender == 'female':
			bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age) + 6
		else:
			print("Invalid input. Please specify 'male' or 'female'.")
			return None
		return bmr
		
	def daily_calorie_goal(self):
		bmr = self.calculate_bmr()
		if bmr is None:
			return None
		if self.goal == 'gain':
			daily_calories = bmr * 1.2 
		elif self.goal == 'lose':
			daily_calories = bmr * 0.8
		elif self.goal == 'maintain':
			daily_calories = bmr
		else:
			print("This is not a goal. Choose from 'gain', 'lose', or 'maintain'.")
			return None
		return daily_calories
	
	def get_age(self):
		if self.age <= 18:
			print("This calculator is for adults (18+). Enter a valid age.")
	
	def add_to_file(self, filename):
		with open(filename, 'a') as file:
			file.write(f'Fitness goal: {self.goal} Cals/day: {self.daily_calorie_goal()}')
