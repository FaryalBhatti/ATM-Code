print("Welcome To ATM")
name = "Ali"
password = 7272

entern = (input("Enter your name :"))
enterp = int(input("Enter your Password :"))

if (entern==name) & (enterp==password):
    condition = True
else:
    condition = False
    print("Your password or name is incorrect")

total=500

while condition:

    print("Choose the following options to proceed")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Exit")
    enter = int(input("Select any option :"))

    if enter==1:
        print("Withdraw")
        baharnikalna=int(input("Enter the amount which you have to withdraw :"))
        if baharnikalna<=total:
          total=total-baharnikalna
          print("Now your current amount is {0}".format(total))
        else:
            print("Your balance is less then the amount u entered")
    elif enter==2:
        print("Desposit")
        deposit=int(input("Enter the amount which you have to deposit :"))
        total=deposit+total
        print("Now your current amount is {0}".format(total))
    elif enter==3:
        print("Exit")
        condition=False
    else:
        print("Wrong option please try again")