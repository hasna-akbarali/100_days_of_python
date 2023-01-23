logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def addition(a,b):
    result = a + b
    print(f'{a} + {b} = {a+b}')
    return result

def subtract(a,b):
    result = a - b
    print (f'{a} - {b} = {a-b}')
    return result

def multiply(a,b):
    result = a * b
    print (f'{a} * {b} = {a*b}')
    return result

def divide(a,b):
    result = a / b
    print (f'{a} / {b} = {a/b}')
    return result

def calculator():
    
    num1 = float(input("Whats the first number? "))
    
    operations = {'+': addition,'-': subtract,'*': multiply,'/': divide}
    
    should_continue = True
    
    while(should_continue == True):
        for i in operations:
            print(i)
        op = input("Pick an operation: ")

        num2 = float(input("Whats the next number? "))

        calculation_function = operations[op]
        result = calculation_function(num1,num2)

        if (input(f'Type \'y\' to continue with {result} or type \'n\' to start a new calculation') == 'y'):
            num1 = result
        else :
            should_continue = False
            clear()
            calculator()
            
print(logo)
calculator()
