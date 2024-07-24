# age = input('enter your age: ')

# if age.isdigit():
    # print('the age is a number')
    # age = int(age)

    # if age >= 0 and age <= 2:
    # if 0 <= age <= 2:
        # print('you are a baby')
    # elif 3 <= age <=12:
        # print('you are a child')
    # else:
        # print('pass age')
# else:
    # print('the age is not a number')



...
A1 = 75 - 100
B2 = 70 - 74
B3 = 65 - 69
C4 = 60 - 64
C5 = 55 - 59
C6 = 50 - 54
D7 = 45 - 49
E8 = 40 - 44
F9 = 0 - 39

# Write a program that takes user input between 0-100 and return the expected grade.

# E.G 
# your result score of 57 is C5 

# not. use a loop control statement in your program 
 

user_score = (input('enter the grade:'))
print(user_score.isdigit())

def determine_grade(score):
    if score <= 75 and score >= 100:
        return 'A1'
    elif score == 70:
        return 'B2'
    elif score >= 65 and score <= 69:
        return 'B3'
    elif score >= 60 and score <= 64:
        return 'C4'
    elif score >= 55 and score <= 59:
        return 'C5'
    elif score >= 50 and score <= 54:
        return 'C6'
    elif score >= 45 and score <= 49:
        return 'D7'
    elif score >= 40 and score <= 44:
        return 'E8'
    else:
        return 'F9'
    
# loop to ensure valid input
    while True:
        try:
            user_score = int(input('enter the score'))
            if user_score < 0 or user_score > 100:
                print('invalid input. enter a valid score')
            else:
                break
        except ValueError:
            print('invalid input. enter a valid score')

# determining the grade based on the input score 
grade = determine_grade(user_score)
print(f'result score of {user_score}is{grade}') 
''''''
