logo =  '''
 _____________________
|  _________________  |
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
print(logo)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2  
def division(n1,n2):   
    return n1/n2

operators ={
             "+":add, "-":subtract, "*": multiply, "/": division  
            }
def calculator():
    should_countinue = True
    num1 =int(input("Please enter the first number: "))
    while should_countinue: 
        for operator in operators:
            print(operator)    
        operation_symbol =input("enter a symbol from above: ")
        num2 =int(input("Please enter the next number: "))
        calclulation_function = operators[operation_symbol]
        result = calclulation_function(num1, num2)
        print(f"The calculation of {num1}{operation_symbol}{num2} is {result} ")
        if input(f"Type 'y'to continue calculating with the {result} or type 'n'to type new numbers: ") == 'y':
            should_countinue = True
        else:
            should_countinue = False
            calculator()    

calculator()