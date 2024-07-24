'''
Write a program that takes a list of integers as input and return the sum of all the integers in the list.
'''

def calculate_sum(input_list):
    total_sum=sum(input_list)
    return total_sum
my_list = input('Enter list of integers: ')
result = calculate_sum(my_list)
print(result)


'''
Write a program that takes a list of integers as input and returns the average of all the integers in the list.
'''

def calculate_average(input_list):
    total_sum = sum(input_list)
    average = total_sum/len(input_list)
    return average
my_list = [19, 30, 23, 17, 26]
result = calculate_average(my_list)
print(result)


'''
write a function that takes a strig as input and returns the length of the string.
'''

def string_length(input_string):
    length = len(input_string)
    return length
my_string = 'My name is Adebiyi'
result = string_length(my_string)
print(result)


'''
write a function that takes a list of integers as input and returns the maximum value in the list.
'''

def find_max_value(input_list):
    max_value = max(input_list)
    return max_value
my_list =[19, 30, 23, 17, 26]
result = find_max_value(my_list)
print(result)


'''
write a program that takes a list of integers as input and returns a new list that contains only the even integers from the original list.
'''

def filter_even_numbers(input_list):
    even_numbers = [num for num in input_list if num %2 == 0]
    return even_numbers
my_list=[1, 2, 3, 4, 5]
reult = filter_even_numbers(my_list)
print(result)


'''
write a program that takes two lists of intergers as input and returns a new list that contains the intersection of the two lists(i.e, the elements that are present in both lists).
'''

def find_intersection(row1, row2):
    set1 = set(row1)
    set2 = set(row2)
    intersection_list = list(set1.intersection(set2))
    return intersection_list
row1 = [1, 2, 3, 4, 5]
row2 = [3, 4, 5, 6, 7]
result = find_intersection(row1, row2)
print(result) 


'''
Write a program that takes a list of integers as input and returns a new list that contains the squares of all the integers in the original list.
'''

def square_integers(input_list):
    squared_list = [num*num for num in input_list]
    return squared_list
my_list = [19, 30, 23, 17, 26]
result = square_integers(my_list)
print(result)


'''
Write a function that takes two integers as input and returns the sum of the two integer
'''

def addNum(num1, num2):
    result = num1 + num2
    print(result)

addNum(43, 34)


'''
Write a program that takes a list of integers as input and returns the product of all the integers in the list 
'''

def calculate_product(input_list):
    product = 1
    for num in input_list:
        product *= num
        return product
    my_list = [2, 3, 4]
    result = calculate_product(my_list)
    print(result)


'''
Write a program that takes a list of strings as input and returns a new list that contains only the strings that stat with the letter 'a'
'''

def filter_strings(input_list):
    filtered_list = [string for string in input_list if string.startswith('a')]
    return filtered_list

my_strings = ["Adebiyi", "Bolu", "Sola", "Kiwi", "Adeyoju"]
filtered_result = filter_strings(my_strings)
print(filtered_result)