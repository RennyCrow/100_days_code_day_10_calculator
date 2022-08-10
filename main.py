from art import logo
import os


def sum(n1:float, n2:float) -> float:
    return n1 + n2


def subtration(n1:float, n2:float) -> float:
    return n1 - n2


def multiplication(n1:float, n2:float) -> float:
    return n1 * n2


def division(n1:float, n2:float) -> float:
    if n2 == 0:
        return n1

    return n1 / n2


operations = {
    '+': sum,
    '-': subtration,
    '*': multiplication,
    '/': division,
}


def calculator() -> None:
    print(logo)
    is_calculating = True
    first_number = float(input("Type the first number: "))

    for operation in operations:
        print(operation)

    while is_calculating:
        selected_operation = input("Pick a operation: ")
        next_number = float(input("Type the next value: "))    
        result = operations[selected_operation](first_number, next_number)
    
        print(f"{first_number} {selected_operation} {next_number} = {result}")
    
        keep_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'e' to close the app: ")

        if keep_calculating == 'y':
            first_number = result
        elif keep_calculating == 'n':
            os.system("clear")
            calculator()
            is_calculating = False
        else:
            is_calculating = False


calculator()
