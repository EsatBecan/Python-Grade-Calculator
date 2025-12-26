year = 2025
birth_year = int(input("What year were you born?:\n"))
future = int(input("How many years into the future do you want to calculate?:\n"))

age = year - birth_year
grade = age - 5
start_year = birth_year + 6
uni_grade = age - 17
future_grade = grade + future
future_age = age + future
future_uni_grade = future_age - 17

print("Your current age is", age ,".", future , "years later, you will be", future_age, "years old\n")

if 0 < grade <= 12:
	print("You are currently in grade" , grade , ", you started school in" , start_year , "\n")
elif 1 > grade:
	years_left = 6 - age
	print("You haven't started school yet, you have" , years_left, "years left to start\n")
elif 18 >= grade > 12:
	uni_grade = age - 17
	print("You are in university year", uni_grade, "\n")
elif grade > 18:
	years_since = uni_grade - 6
	print("It has been" , years_since , "years since you graduated university\n")


if 0 < future_grade <= 12:
	print(future, "years later you will be in grade" , future_grade , ", you started school in" , start_year , "\n")
elif 1 > future_grade:
	future_years_left = 6 - future_age
	print("You won't have started school yet, you have" , future_years_left, "years left to start\n")
elif 18 >= future_grade > 12:
	future_uni_grade = future_age - 17
	print(future, "years later you will be in university year", future_uni_grade, "\n")
elif future_grade > 18:
	future_years_since = future_uni_grade - 6
	print(future, "years later it will be" , future_years_since , "years since you graduated university\n")
  
