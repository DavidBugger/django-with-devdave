# variable declarations 
# exploring data types 

name = "Femi" 

dob = 1993 

year = 2025

weight = 34.0 

is_student = True 

# calculate age
age = year - dob

gender = 'male'

# print (" My name is ", name , "\n and my age is " , str(age) ," \n and my weight is " , str(weight) , "kg" + "\n and I am a student: " ,str(is_student))

# truth table AND GATE
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0 
# 0 0 = 0

# OR GATE 
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0


# collect user date of birth and calculate age
date_of_birth = int(input("Enter your year of birth: "))
gender = str(input("Gender Please: "))

new_age = year - date_of_birth
# checking eligibility of student 
if new_age >= 18  or  gender != gender:
    print(f" Your age is: {new_age} \n Course Eligibility: You are eligible to enroll for the course")
else:
    print("You are not eligible to enroll for the course")
    


