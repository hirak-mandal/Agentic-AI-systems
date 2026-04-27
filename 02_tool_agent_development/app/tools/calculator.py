def calculator(expression: str):
    try:
        return eval(expression)
    except:
        return "Error"