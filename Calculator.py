# Calculator

# Addition
def add(n1,n2):
    return n1+n2

# Substraction
def sub(n1,n2):
    return n1-n2

# Multiplication
def mult(n1,n2):
    return n1*n2

# Division
def divide(n1,n2):
    return n1/n2

# Dictionary of operations
Operation= {
    "+":add,  
    "-":sub,
    "*":mult,
    "/":divide
            }

# main function

def calc():
        
    num1=float(input("What's the first number? :"))

    # Printing all the operations in Dictionary
    for  operator in Operation:
        print(operator)

    operation=input("Which operation do you wanna perform? :")
    num2=float(input("What's the Second number? :"))

    answer_01=Operation[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {answer_01}")

    # Agian Performing calcultion with the above answer
    calculate=input(f"Type 'y' to continue calculating with {answer_01}, or type 'n' to start again :")
    if calculate=="y":
            
        while calculate=="y":
            operation_symbol=input("Pick an operation: ")
            num3= float(input("What's the next number? :"))
            answer_02=Operation[operation_symbol](answer_01,num3)
            print(f"{answer_01} {operation_symbol} {num3} = {answer_02}")
            answer_01=answer_02
            calculate=input(f"Type 'y' to continue calculating with {answer_02}, or type 'n' to exit. :")
    elif calculate=="n":
        calc()
    else:
        print("Invalid Input!!! You got exiled!!!")

calc()