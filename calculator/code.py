answer = "yes"
while answer == "yes":
    print ('Select an operation to perform:')
    print ('1. ADD')
    print ('2. SUBTRACT')
    print ('3. MULTIPLY')
    print ('4. DIVIDE')
    operation = input()

    if operation == "1":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The result equals to " + str(int(num1) + int(num2)))
        print("Do you want to use calculator one more time?")
        answer = input()
        if answer == "yes":
            continue
        else:
            break
    elif operation == "2":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The result equals to " + str(int(num1) - int(num2)))
        print("Do you want to use calculator one more time?")
        answer = input()
        if answer == "yes":
            continue
        else:
            break
    elif operation == "3":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The result equals to " + str(int(num1) * int(num2)))
        print("Do you want to use calculator one more time?")
        answer = input()
        if answer == "yes":
            continue
        else:
            break
    elif operation == "4":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The result equals to " + str(int(num1) / int(num2)))
        print("Do you want to use calculator one more time?")
        answer = input()
        if answer == "yes":
            continue
        else:
            break
    else:
        print('Invalid Entry')
        print("Do you want to use calculator one more time?")
        answer = input()
        if answer == "yes":
            continue
        else:
            break