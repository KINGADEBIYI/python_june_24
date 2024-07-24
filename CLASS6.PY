import math 

def myprogram():
    print('welcome to our software !!!!')
    print('''
        CHOOSE THE NUMBER OF YOUR OPTION BELOW:
          1. perform an arithemetic operation.
          2. perform a temperature conversion.
          3. perform a currency conversion
          4. close program.
          ''')
    option = input('enter your option: ')

    if option == '1':
        print('perfom an arithemetic operation. \n\n')
        print('''
            ENTER THE SYMBOL FOR YOUR OPERATION BELOW:
              1. ADDITION       +
              2. SUBTRACTION    -
              3. MULTIPLICATION *
              4. DIVISION       /
              5. SQUARE ROOT
        ''')
        op_list = ['+', '-', '=', '/']
        operation = input('enter operation number: ')
        num1 = input('enter number: ')

        if operation.strip() in op_list:
            num2 = input('enter second number: ')
            print('\n')
            try:
                print(eval(num1+operation+num2))

            except:
                print('you have entered an invalid value\n\n')
        elif operation == '5':
            print('perform square root')
            try:
                # print(math.sqrt(int(num1)))
                print(round(math.sqrt(int(num1))), 1)
                print('\n')
            except:
                print('you have entered an invalid value\n\n')



        # if operation == '1':
                # result = int(num1) + int(num2)
                # resullt = eval(num1+'+'+num2)
                # '7+8'
                # print(result)
            # recursive
            myprogram()
    elif option == '2':
        print('perform a temperature convertion. \n\n')
        myprogram()
    elif option == '3':
        print('perform a currency convertion\n\n')
        myprogram()
    else:
        print('thank you for using our program.')
        pass

# myprogram()
    

# def destroy():
    # print ('destructive code !!!!!!!!!!!!!!!\n')
    # try:
        # destroy()
    # except recursionError:
            # print('Exception checked !!!!!!!!!!!!!!\n')
            # destroy()
    
# destroy()
    
'''
Write a program that takes a list or range of numbers.
1. checks if the number is an odd or even number.
    14 -even
    15 -odd
2. Below
    checks if the is divisible by 3 and print (fizz)
    check if the number is divisible by 5 and print (buzz)
    check if it's divisible by both 3 and 5, print(fizzbuzz)
    if not divisible by any, print the number

create a list of at least 5 states and capital
write a program collects user option 1-4
1. displays all states and capital
2. add new state and capital
3. edit a particular state and capital
4. delete a particular state and capital
'''
for i in range(1, 11):
    if i%2 == 0:
        print(f'{i} - even')
    else:
        print(f'{i} - odd')

for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i) 