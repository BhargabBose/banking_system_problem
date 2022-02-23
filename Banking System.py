#Q3) Design a banking system. Make global tuples array of structure (AccountNum, Balance)
#When you run the code, it should show a start screen like this
#===============================
#	   Boss Man Banker
#===============================
# Choose Option:
#1) View Balance
#2) Deposit Money <-- Just an input so don't really care
#3) Withdraw Money
#4) Close program
#Enter your selection: (THIS IS WHERE YOU PUT THE OPTIONS)
#Notes: Make seperate functions for each option. And dont fuck it up. Don't forget to initialize with your account/

# Made by Bhargab "BossMan" Bose
# Licence Open-source

Dict = dict({"AccountNum":1, "Balance":69 })     # Learn the use of Dictionary

def View_Balance():
    global Dict
    print(str(Dict["Balance"]))

def Deposit_Money():
    global Dict
    Deposit = input("Enter the amount you want to deposit: ")
    (Dict["Balance"]) = int(Deposit) + (Dict["Balance"])
    print("Current Balance in your account is " + str((Dict["Balance"])))

def Withdraw_Money():
    global Dict
    Withdraw = int(input("Enter the amount you want to withdraw: "))
    if (Dict["Balance"]) >= Withdraw:
        (Dict["Balance"]) = (Dict["Balance"]) - int(Withdraw)
        print("Current Balance in your account is " + str((Dict["Balance"])))
    else:
        print("Not enough funds ")

def Close_Program():
    print("Thank you for banking with us.")
    quit()

def Start_Screen():
    print("===============================")
    print("         Boss Man Bank         ")
    print("===============================")
    print("Choose an Option from the list below:")
    print("1) View Balance")
    print("2) Deposit Money")
    print("3) Withdraw Money")
    print("4) Close program")
    Choice = int(input("Enter your choice: "))
    if Choice == 1 :
        View_Balance()
    elif Choice == 2:
        Deposit_Money()
    elif Choice == 3:
        Withdraw_Money()
    elif Choice == 4:
        Close_Program()
    else:
        print("Invalid Choice")
    Start_Screen()

Start_Screen()




