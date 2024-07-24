...
# UI admission vs OAU
# Baby =
...

scoreLT = [75, 70, 65, 60, 55, 50, 45, 40]
grade = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9']
# print(grade[0])
# student_score = input('Enter student score: ')
student_score = '54'
# print(type(student_score))

# if student_score.isnumeric():
    # student_score = int(student_score)
    # pass
# print(scoreLT.index('D7')) = 5
print(scoreLT[5])
try:
    student_score = int(student_score)
    # print(type(student_score))

    if student_score >= 0 and student_score <= 100:
    # if 0 <= student_score <= 100:
        print('student score is valid...')
        for eachitem in scoreLT:
            pos = scoreLT.index(eachitem)
            print(pos, f'the index of {eachitem} - {grade[pos]}')

            if student_score >= eachitem:
                print(f'the grade of {student_score}is {grade[pos]}')
                pass
                break
            elif student_score < 40:
                print(f'the grade of {student_score} is {grade[-1]}')
                pass
            pass
    else:
        print('student score is invalid...')

        pass

except:
    print('''
          you have input an incorrect value...
          check student score again...
          ''')
    pass



# function
# A function is a block of reusesable code that runs only when called, it can also take argument as a parameter
def greet():
    print('Hello world !')

greet ()
greet ()
greet ()
greet ()


def greetstudent(name):
# parameter is the requiremnet
    print(f'Hello{name}, welcome to class')

greetstudent('Touch')
# argument: details

greetstudent('Tunez')
greetstudent('Leke')
greetstudent('Adebiyi')
greetstudent('Adex')

def addNum(num1, num2):
    result = num1 + num2
    print(result)

addNum(43, 34)


def subNum(num1, num2):
    result = num1 - num2
    print(result)

    subNum(43, 34)

def mulNum(num1, num2):
    result = num1 * num2
    print(result)

    mulNum(43, 34)

def divNum(num1, num2):
    result = num1 / num2
    print(result)

    divNum(43, 34)

'''
write a program that performs an arithemetic function on two numbers based on user option
    
write a temperature converter program, fehenreit to celcius and vice evrsa
    
write a program that converts dollar to naira and vice versa, using 1640 naira to a dollar as exchange rate
'''

