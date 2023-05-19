#this function adds numbers
def add(x, y):
    return x + y

#this function subtracts numbers

def subtract(x, y):
    return x - y

#this function multiplies numbers
def multiply(x, y):
    return x * y

#this function divides numbers
def divide(x, y):
    return x / y

print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #take input from user 
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input. Please enter a number")
            continue
    

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    
    elif choice =='2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    
    elif choice == "3": 
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))


    ##check if the user wants to do another calculation
    next_calculation = input("Enter choice (1/2/3/4) or Enter 'end': ")
    if next_calculation == "end":
        break
    else:
        print("Invalid Input")

