# Welcome to the first python class

...

# outlines
# Variables / Values / Operators

    # Strings
    # Integer; Numbers, Float, Complex
    # Collection; List, Tuple, Set, Dict

# Control Statement
    # Conditional Statement
    # Loops / Iteration

# Funtion
# Classes
# Project

...
# = is an assignment operator
# A varible is a comtainer that holds value
# Value is the same thing as Data

x = 5

y = 10

print(x)


# Operators
# Arithemetic Operators

print(x + y) 
# Addition

print(x - y)
# Subtraction

print(x * y)
# Multiplication

print(x / y)
# Division


name = 'Boluwatife'
name2 = 'Parach'
name3 = 'Aishat'
statement1 = 'Hello, welcome to the first python class'

statement2 = 'He`s coming to the party'
print(statement2)

statement3 = 'he/`s coming tO tHe pARty'
print(statement3)

print(name[0])
print(name[1])

print(name[6:10])

print(statement3[-1])
print(statement3[-5: -1])
print(statement3[-5: ])
print(name[ :6])

# string methods
# methods are python ready-made function that we can use to manuveura data

print(statement3.capitalize())
# converts the first character to upper case

print(statement3.upper())
# converts all character to capital letters 

print(statement3.lower())
# converts all characters to lower letter

y = 10
x = 3

result = y - x

a = 'parach'
b = 'samuel'

print(a[0])
print('')
print('')
print('')

Animals = ['Goats', 'Gorilla', 'Fish', 'Frog', 'Lizard']
for i in Animals:
    # print(i +  is an animal)
    print(i[0])
    if i[0] == 'G':
        print(i)