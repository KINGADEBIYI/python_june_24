student_list = ['Adebiyi', 'Aishat', 'Leke', 'Fortune', 'Adewumi', 'Boluwatife']
# Hello Adebiyi, Welcome to class

name = 'john'
concat = 'hello' + name 
# concentration
print(concat)

for eachstudent in student_list:
    #  print('hello' + eachstudent + ', welcome to class')
    #  print('hello', eachstudent, 'welcome to class')
    #  print('hello' + eachstudent + ' , welcome to class')
     print(f'hello {eachstudent}, welcome to class')
    # f-string/format-string
     
result = 'd'

if result == 'a':
     print('the code execution is successful')

elif result == 'b':
     print('the code execution is successful with little error')

elif result == 'c':
     print('the code execution is successful with error')

elif result == 'd':
     print('the code execution is successful with lots of error')

else:
     print('the code failed.')

print('')
print('')


person1 = input('enter name of student: ')
print(person1)
print(person1[0])
print(person1[:3])
print(type(person1))
# input is used to create value through the terminal

student_list.append(person1)
print(student_list)
# append is used to add to a variable

# casting - a way of changing data types
num = 3
print(type(num))
num = str(num)

print(type(num))
print('')

item2 = '36'

print(type(item2))
item2 = int(item2)

print(type(item2))

num1 = 10
num2 = 17

if num1 <7 and num2 <20:
     print('condition met')

if num1 == 10 or num2 <15:
     print('condition met')


...
# class task
# 1.) UI requires students to have 50% or above in both english and math to be considered, 
# OAU requires students to have at least 50% or more in either english or math to be 
# considered.


def check_admission(english_score, math_score):
     # for UI requirement
     UI_pass = english_score>=50 and math_score>=50

     # for OAU requirement
     OAU_pass = english_score>=50 or math_score>=50
     return UI_pass, OAU_pass
english_score = 60
math_score = 45
UI_requirements, OAU_reqrements = check_admission(english_score, math_score)
print('meets UI requirements', UI_requirements)
print('meets OAU requirement', OAU_reqrements)


# 2.) Baby = 0-2
# children = 3-12
# teen = 13-17
# adult = 18-29
# older adult = 46-70

# request user age, and return the age group based on the input.

def determine_age_group(age):
     if age>0 and age <2:
          return 'Baby'
     elif age>=3 and age<=12:
          return 'Children'
     elif age>=13 and age<=17:
          return 'Teen'
     elif age>=18 and age<=29:
          return 'youth'
     elif age>=30 and age<=45:
          return 'Adult'
     elif age>=46 and age<=70:
          return 'Older Adult'
     else:
          return 'Unknown'

# requesting user input determine 
user_age = (input('enter the age:'))
print(user_age.isdigit())

# determining the age
# age_group = determine_age_group(user_age)


# print('based on the age group provided, you belong to the age group:', age_group)


...
