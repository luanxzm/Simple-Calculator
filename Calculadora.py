while True:
    operation = int(input('''Which operation do you want to perform?
    1) Addition
    2) Subtraction
    3) Division
    4) Multiplication
 '''))
    # First Operation
    if operation == 1:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        t1 = n1 + n2
        print(f'Your result is {t1:.2f}!!')
    # Second Operation
    elif operation == 2:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        t1 = n1 - n2
        print(f'Your result is {t1:.2f}!!')
    # Third Operation
    elif operation == 3:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        if n2 == 0:
            print('Division by 0 is not allowed.')
        else:
            t1 = n1 / n2
            print(f'Your result is {t1:.2f}!!')
    # Fourth Operation
    elif operation == 4:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
        t1 = n1 * n2
        print(f'Your result is {t1:.2f}!!')
    reset = int(input('''Do you want to use the calculator again?
    1) Yes
    2) No
     '''))
    # Reset
    if reset != 1:
        print('Calculator Closed!!')
        break