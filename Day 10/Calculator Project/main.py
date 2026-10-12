import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Add these 4 functions to a dictionary
calculator_dic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    should_to_continue = True
    f_number = float(input("Type your first number\n"))

    while should_to_continue:

        for symbol in calculator_dic:
            print(symbol)
        user_choice = input("Choose your math operator\n")

        s_number = float(input("Type the second number\n"))

        result = calculator_dic[user_choice](f_number,s_number)

        print(f"{f_number} {user_choice} {s_number} = {result}")

        to_continue = input("Type 'y' to continue with the previous result or type 'n' to start with a new number\n").lower()

        if to_continue == "y":
            f_number = result
        else:
            print("\n" * 30)
            calculator()

calculator()