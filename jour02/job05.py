def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    else:
        return ("erreur")
    print(result)

calcule(3,"+", 4)
calcule(390, "-", 1)
calcule(45, "/", 3)
calcule(3049, "*", 13)
calcule(738, "%", 30)