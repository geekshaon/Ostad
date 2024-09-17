#Simple calculator v1.1
#Mehedi Hasan

def addition(a,b):
    print(f'Addition: {a} + {b} = {a+b}')
def subtraction(a,b):
    print(f'Subtraction: {a} - {b} = {a-b}')

def multiplication(a,b):
    print(f'Multiplication: {a} * {b} = {a*b}')

def division(a,b):
    try:
        print(f'Division: {a} / {b} = {round(a/b,2)}')
    except ZeroDivisionError:
        print("You can't divide by zero")
def modulus(a,b):
    try:
        print(f'Modulus: {a} % {b} = {a%b}')
    except Exception as e:
        print(e, ", You can not use zero for modulus")


print(f"Select operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide\n 5. Modulus")

while True:
    try:
        option = int(input('Enter choice (1/2/3/4/5):'))
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        break
    except ValueError:
        print('Must enter valid number')

if option == 1:
    addition(num1, num2)
elif option == 2:
    subtraction(num1, num2)
elif option == 3:
    multiplication(num1, num2)
elif option == 4:
    division(num1, num2)
elif option == 5:
    modulus(num1, num2)
else:
    print('you should enter a number between 1 and 5')




