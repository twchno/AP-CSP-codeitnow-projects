#dylan King
#22/10/25
#truthtable

num1 = float(input("Enter your first number: \n"))
num2 = float(input("Enter your second number: \n"))
option_1 = "0"
option_2 = "0"

def main1():
    global num1
    global num2
    global option_1
    global option_2
    if option_1 == "greater than" and option_2 == "less than":
        if num1 > num2 and num1 < num2:
            print(f"{num1} is greater than {num2} and {num1} is less than {num2}")
        else:
            print(f"{num1} is not greater than {num2} or {num1} is not less than {num2}")
    elif option_1 == "greater than" and option_2 == "greater than or equal to":
        if num1 > num2 and num1 >= num2:
            print(f"{num1} is greater than {num2} and {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} or {num1} is not greater than or equal to {num2}")
    elif option_1 == "greater than" and option_2 == "less than or equal to":
        if num1 > num2 and num1 <= num2:
            print(f"{num1} is greater than {num2} and {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} or {num1} is not less than or equal to {num2}")
    elif option_1 == "greater than" and option_2 == "equal to":
        if num1 > num2 and num1 == num2:
            print(f"{num1} is greater than {num2} and {num1} is equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} or {num1} is not equal to {num2}")
    elif option_1 == "greater than" and option_2 == "not equal to":
        if num1 > num2 and num1 != num2:
            print(f"{num1} is greater than {num2} and {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} or {num1} is equal to {num2}")
    elif option_1 == "less than" and option_2 == "greater than":
        if num1 < num2 and num1 > num2:
            print(f"{num1} is less than {num2} and {num1} is greater than {num2}")
        else:
            print(f"{num1} is not less than {num2} or {num1} is not greater than {num2}")
    elif option_1 == "less than" and option_2 == "greater than or equal to":
        if num1 < num2 and num1 >= num2:
            print(f"{num1} is less than {num2} and {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} or {num1} is not greater than or equal to {num2}")
    elif option_1 == "less than" and option_2 == "less than or equal to":
        if num1 < num2 and num1 <= num2:
            print(f"{num1} is less than {num2} and {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} or {num1} is not less than or equal to {num2}")
    elif option_1 == "less than" and option_2 == "equal to":
        if num1 < num2 and num1 == num2:
            print(f"{num1} is less than {num2} and {num1} is equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} or {num1} is not equal to {num2}")
    elif option_1 == "less than" and option_2 == "not equal to":
        if num1 < num2 and num1 != num2:
            print(f"{num1} is less than {num2} and {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} or {num1} is equal to {num2}")
    elif option_1 == "greater than or equal to" and option_2 == "greater than":
        if num1 >= num2 and num1 > num2:
            print(f"{num1} is greater than or equal to {num2} and {num1} is greater than {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} or {num1} is not greater than {num2}")
    elif option_1 == "greater than or equal to" and option_2 == "less than":
        if num1 >= num2 and num1 < num2:
            print(f"{num1} is greater than or equal to {num2} and {num1} is less than {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} or {num1} is not less than {num2}")
    elif option_1 == "greater than or equal to" and option_2 == "less than or equal to":
        if num1 >= num2 and num1 <= num2:
            print(f"{num1} is greater than or equal to {num2} and {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} or {num1} is not less than or equal to {num2}")
    elif option_1 == "greater than or equal to" and option_2 == "equal to":
        if num1 >= num2 and num1 == num2:
            print(f"{num1} is greater than or equal to {num2} and {num1} is equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} or {num1} is not equal to {num2}")
    elif option_1 == "greater than or equal to" and option_2 == "not equal to":
        if num1 >= num2 and num1 != num2:
            print(f"{num1} is greater than or equal to {num2} and {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} or {num1} is equal to {num2}")
    elif option_1 == "less than or equal to" and option_2 == "greater than":
        if num1 <= num2 and num1 > num2:
            print(f"{num1} is less than or equal to {num2} and {num1} is greater than {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} or {num1} is not greater than {num2}")
    elif option_1 == "less than or equal to" and option_2 == "less than":
        if num1 <= num2 and num1 < num2:
            print(f"{num1} is less than or equal to {num2} and {num1} is less than {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} or {num1} is not less than {num2}")
    elif option_1 == "less than or equal to" and option_2 == "greater than or equal to":
        if num1 <= num2 and num1 >= num2:
            print(f"{num1} is less than or equal to {num2} and {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} or {num1} is not greater than or equal to {num2}")
    elif option_1 == "less than or equal to" and option_2 == "equal to":
        if num1 <= num2 and num1 == num2:
            print(f"{num1} is less than or equal to {num2} and {num1} is equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} or {num1} is not equal to {num2}")
    elif option_1 == "less than or equal to" and option_2 == "not equal to":
        if num1 <= num2 and num1 != num2:
            print(f"{num1} is less than or equal to {num2} and {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} or {num1} is equal to {num2}")
    elif option_1 == "equal to" and option_2 == "greater than":
        if num1 == num2 and num1 > num2:
            print(f"{num1} is equal to {num2} and {num1} is greater than {num2}")
        else:
            print(f"{num1} is not equal to {num2} or {num1} is not greater than {num2}")
    elif option_1 == "equal to" and option_2 == "less than":
        if num1 == num2 and num1 < num2:
            print(f"{num1} is equal to {num2} and {num1} is less than {num2}")
        else:
            print(f"{num1} is not equal to {num2} or {num1} is not less than {num2}")
    elif option_1 == "equal to" and option_2 == "greater than or equal to":
        if num1 == num2 and num1 >= num2:
            print(f"{num1} is equal to {num2} and {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} or {num1} is not greater than or equal to {num2}")
    elif option_1 == "equal to" and option_2 == "less than or equal to":
        if num1 == num2 and num1 <= num2:
            print(f"{num1} is equal to {num2} and {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} or {num1} is not less than or equal to {num2}")
    elif option_1 == "equal to" and option_2 == "not equal to":
        if num1 == num2 and num1 != num2:
            print(f"{num1} is equal to {num2} and {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} or {num1} is equal to {num2}")
    elif option_1 == "not equal to" and option_2 == "greater than":
        if num1 != num2 and num1 > num2:
            print(f"{num1} is not equal to {num2} and {num1} is greater than {num2}")
        else:
            print(f"{num1} is equal to {num2} or {num1} is not greater than {num2}")
    elif option_1 == "not equal to" and option_2 == "less than":
        if num1 != num2 and num1 < num2:
            print(f"{num1} is not equal to {num2} and {num1} is less than {num2}")
        else:
            print(f"{num1} is equal to {num2} or {num1} is not less than {num2}")
    elif option_1 == "not equal to" and option_2 == "greater than or equal to":
        if num1 != num2 and num1 >= num2:
            print(f"{num1} is not equal to {num2} and {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} or {num1} is not greater than or equal to {num2}")
    elif option_1 == "not equal to" and option_2 == "less than or equal to":
        if num1 != num2 and num1 <= num2:
            print(f"{num1} is not equal to {num2} and {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} or {num1} is not less than or equal to {num2}")
    elif option_1 == "not equal to" and option_2 == "equal to":
        if num1 != num2 and num1 == num2:
            print(f"{num1} is not equal to {num2} and {num1} is equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} or {num1} is not equal to {num2}")
        


def main2():
    global num1
    global num2
    global option_1
    global option_2
    if option_1 == "greater than" or option_2 == "less than":
        if num1 > num2 or num1 < num2:
            print(f"{num1} is greater than {num2} or {num1} is less than {num2}")
        else:
            print(f"{num1} is not greater than {num2} and {num1} is not less than {num2}")
    elif option_1 == "greater than" or option_2 == "greater than or equal to":
        if num1 > num2 or num1 >= num2:
            print(f"{num1} is greater than {num2} or {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} and {num1} is not greater than or equal to {num2}")
    elif option_1 == "greater than" or option_2 == "less than or equal to":
        if num1 > num2 or num1 <= num2:
            print(f"{num1} is greater than {num2} or {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} and {num1} is not less than or equal to {num2}")
    elif option_1 == "greater than" or option_2 == "equal to":
        if num1 > num2 or num1 == num2:
            print(f"{num1} is greater than {num2} or {num1} is equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} and {num1} is not equal to {num2}")
    elif option_1 == "greater than" or option_2 == "not equal to":
        if num1 > num2 or num1 != num2:
            print(f"{num1} is greater than {num2} or {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not greater than {num2} and {num1} is equal to {num2}")
    elif option_1 == "less than" or option_2 == "greater than":
        if num1 < num2 or num1 > num2:
            print(f"{num1} is less than {num2} or {num1} is greater than {num2}")
        else:
            print(f"{num1} is not less than {num2} and {num1} is not greater than {num2}")
    elif option_1 == "less than" or option_2 == "greater than or equal to":
        if num1 < num2 or num1 >= num2:
            print(f"{num1} is less than {num2} or {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} and {num1} is not greater than or equal to {num2}")
    elif option_1 == "less than" or option_2 == "less than or equal to":
        if num1 < num2 or num1 <= num2:
            print(f"{num1} is less than {num2} or {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} and {num1} is not less than or equal to {num2}")
    elif option_1 == "less than" or option_2 == "equal to":
        if num1 < num2 or num1 == num2:
            print(f"{num1} is less than {num2} or {num1} is equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} and {num1} is not equal to {num2}")
    elif option_1 == "less than" or option_2 == "not equal to":
        if num1 < num2 or num1 != num2:
            print(f"{num1} is less than {num2} or {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not less than {num2} and {num1} is equal to {num2}")
    elif option_1 == "greater than or equal to" or option_2 == "greater than":
        if num1 >= num2 or num1 > num2:
            print(f"{num1} is greater than or equal to {num2} or {num1} is greater than {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} and {num1} is not greater than {num2}")
    elif option_1 == "greater than or equal to" or option_2 == "less than":
        if num1 >= num2 or num1 < num2:
            print(f"{num1} is greater than or equal to {num2} or {num1} is less than {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} and {num1} is not less than {num2}")
    elif option_1 == "greater than or equal to" or option_2 == "less than or equal to":
        if num1 >= num2 or num1 <= num2:
            print(f"{num1} is greater than or equal to {num2} or {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} and {num1} is not less than or equal to {num2}")
    elif option_1 == "greater than or equal to" or option_2 == "equal to":
        if num1 >= num2 or num1 == num2:
            print(f"{num1} is greater than or equal to {num2} or {num1} is equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} and {num1} is not equal to {num2}")
    elif option_1 == "greater than or equal to" or option_2 == "not equal to":
        if num1 >= num2 or num1 != num2:
            print(f"{num1} is greater than or equal to {num2} or {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not greater than or equal to {num2} and {num1} is equal to {num2}")
    elif option_1 == "less than or equal to" or option_2 == "greater than":
        if num1 <= num2 or num1 > num2:
            print(f"{num1} is less than or equal to {num2} or {num1} is greater than {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} and {num1} is not greater than {num2}")
    elif option_1 == "less than or equal to" or option_2 == "less than":
        if num1 <= num2 or num1 < num2:
            print(f"{num1} is less than or equal to {num2} or {num1} is less than {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} and {num1} is not less than {num2}")
    elif option_1 == "less than or equal to" or option_2 == "greater than or equal to":
        if num1 <= num2 or num1 >= num2:
            print(f"{num1} is less than or equal to {num2} or {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} and {num1} is not greater than or equal to {num2}")
    elif option_1 == "less than or equal to" or option_2 == "equal to":
        if num1 <= num2 or num1 == num2:
            print(f"{num1} is less than or equal to {num2} or {num1} is equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} and {num1} is not equal to {num2}")
    elif option_1 == "less than or equal to" or option_2 == "not equal to":
        if num1 <= num2 or num1 != num2:
            print(f"{num1} is less than or equal to {num2} or {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not less than or equal to {num2} and {num1} is equal to {num2}")
    elif option_1 == "equal to" or option_2 == "greater than":
        if num1 == num2 or num1 > num2:
            print(f"{num1} is equal to {num2} or {num1} is greater than {num2}")
        else:
            print(f"{num1} is not equal to {num2} and {num1} is not greater than {num2}")
    elif option_1 == "equal to" or option_2 == "less than":
        if num1 == num2 or num1 < num2:
            print(f"{num1} is equal to {num2} or {num1} is less than {num2}")
        else:
            print(f"{num1} is not equal to {num2} and {num1} is not less than {num2}")
    elif option_1 == "equal to" or option_2 == "greater than or equal to":
        if num1 == num2 or num1 >= num2:
            print(f"{num1} is equal to {num2} or {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} and {num1} is not greater than or equal to {num2}")
    elif option_1 == "equal to" or option_2 == "less than or equal to":
        if num1 == num2 or num1 <= num2:
            print(f"{num1} is equal to {num2} or {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} and {num1} is not less than or equal to {num2}")
    elif option_1 == "equal to" or option_2 == "not equal to":
        if num1 == num2 or num1 != num2:
            print(f"{num1} is equal to {num2} or {num1} is not equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2} and {num1} is equal to {num2}")
    elif option_1 == "not equal to" or option_2 == "greater than":
        if num1 != num2 or num1 > num2:
            print(f"{num1} is not equal to {num2} or {num1} is greater than {num2}")
        else:
            print(f"{num1} is equal to {num2} and {num1} is not greater than {num2}")
    elif option_1 == "not equal to" or option_2 == "less than":
        if num1 != num2 or num1 < num2:
            print(f"{num1} is not equal to {num2} or {num1} is less than {num2}")
        else:
            print(f"{num1} is equal to {num2} and {num1} is not less than {num2}")
    elif option_1 == "not equal to" or option_2 == "greater than or equal to":
        if num1 != num2 or num1 >= num2:
            print(f"{num1} is not equal to {num2} or {num1} is greater than or equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} and {num1} is not greater than or equal to {num2}")
    elif option_1 == "not equal to" or option_2 == "less than or equal to":
        if num1 != num2 or num1 <= num2:
            print(f"{num1} is not equal to {num2} or {num1} is less than or equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} and {num1} is not less than or equal to {num2}")
    elif option_1 == "not equal to" or option_2 == "equal to":
        if num1 != num2 or num1 == num2:
            print(f"{num1} is not equal to {num2} or {num1} is equal to {num2}")
        else:
            print(f"{num1} is equal to {num2} and {num1} is not equal to {num2}")

        #used if user inputs "or"
def coperators_1():
    global option_1
    print("--menu--")
    print("1. greater than(>)")
    print("2. less than(<)")
    print("3. greater than or equal to(>=)")
    print("4. less than or equal to(<=)")
    print("5. equal to(==)")
    print("6. not equal to(!=)")
    print("7. exit")
    choice = input("Pick an option: \n")
    if choice == "1":
        option_1 = "greater than"
        loperator()
    elif choice == "2":
        option_1 = "less than"
        loperator()
    elif choice == "3":
        option_1 = "greater than or equal to"
        loperator()
    elif choice == "4":
        option_1 = "less than or equal to"
        loperator()
    elif choice == "5":
        option_1 = "equal to"
        loperator()
    elif choice == "6":
        option_1 = "not equal to"
        loperator()
    elif choice == "7":
        exit()
    else:
        print("invalid option, try again")
        coperators_1()

def loperator():
    choice1 = input("And or Or? (input as 'and' or 'or'): \n")
    if choice1 == "and":
        coperators_2()
    elif choice1 == "or":
        coperators_3()
    else:
        print("invalid option, try again")
        loperator()

        
        #used if user inputs "and"
def coperators_2():
    global option_1
    global option_2
    print("--AND--")
    print("1. greater than")
    print("2. less than")
    print("3. greater than or equal to")
    print("4. less than or equal to")
    print("5. equal to")
    print("6. not equal to")
    choice1 = str(input("Pick an option: "))
    if choice1 == "1" and option_1 != "greater than":
        option_2 = "greater than"
        main1()
    elif choice1 == "2" and option_1 != "less than":
        option_2 = "less than"
        main1()
    elif choice1 == "3" and option_1 != "greater than or equal to":
        option_2 = "greater than or equal to"
        main1()
    elif choice1 == "4" and option_1 != "less than or equal to":
        option_2 = "less than or equal to"
        main1()
    elif choice1 == "5" and option_1 != "equal to":
        option_2 = "equal to"
        main1()
    elif choice1 == "6" and option_1 != "not equal to":
        option_2 = "not equal to"
        main1()
    else:
        print("invalid option, try again")
        coperators_2()

        #used if user inputs "or"
    

def coperators_3():
    global option_1
    global option_2
    print("--OR--")
    print("1. greater than")
    print("2. less than")
    print("3. greater than or equal to")
    print("4. less than or equal to")
    print("5. equal to")
    print("6. not equal to")
    choice2 = input("Pick an option: ")
    if choice2 == "1" and option_1 != "greater than":
        option_2 = "greater than"
        main2()
    elif choice2 == "2" and option_1 != "less than":
        option_2 = "less than"
        main2()
    elif choice2 == "3" and option_1 != "greater than or equal to":
        option_2 = "greater than or equal to"
        main2()
    elif choice2 == "4" and option_1 != "less than or equal to":
        option_2 = "less than or equal to"
        main2()
    elif choice2 == "5" and option_1 != "equal to":
        option_2 = "equal to"
        main2()
    elif choice2 == "6" and option_1 != "not equal to":
        option_2 = "not equal to"
        main2()
    else:
        print("invalid option, try again")
        coperators_3()

if __name__ == "__main__":
    coperators_1()
