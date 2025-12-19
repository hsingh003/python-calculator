
def Addition(First, Second):
    print("Sum Of The Given Number  :: ", First + Second)


def Subtraction(First, Second):
    print("Subtraction Of The Given Number  :: ", First - Second)


def Multiplication(First, Second):
    print("Product Of The Given Number  :: ", First * Second)


def Division(First, Second):

    if Second == 0:
        print("Cannot divide by zero")
    else:
        print("Division Of The Given Number :: ", First / Second)
def Modulus(First ,Second):
    if Second == 0:
        print("Cannot perform modulus  by zero")
    else:

        print("Modulus of Given Numer :: " ,First%Second)
def Power(First ,Second):
    print("Power Product Is :: " ,First**Second)
def Exit(exit):
    print("Goodbye!")
for i in range(100):
 while True:

        print("\n--- Python Calculator ---")

        print("\nCalculations Times :: ", i + 1)

        try:
            Sign = input("Enter the Sign : (+ - * / % ** ) 'x' is for Exit : = ")
            if Sign == 'x':
                print("GoodBye !")
                break
            First = int(input("Enter the 1st number = "))
            Second = int(input("Enter the 2nd number = "))

        except ValueError:
            print("Invalid Error, Or It will be Number error :: ")
            continue


        if Sign == '+':
            Addition(First, Second)
        elif Sign == '-':
            Subtraction(First, Second)
        elif Sign == '*':
            Multiplication(First, Second)
        elif Sign == '/':

            Division(First, Second)
        elif Sign == '%':
            Modulus(First, Second)
        elif Sign == '**':
            Power(First, Second)
        else:
            print("Invalid Operator ")


