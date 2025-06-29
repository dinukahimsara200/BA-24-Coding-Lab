def is_valid_expression(e):
    stack = []
    opening = "([{"
    closing = ")]}"
    for char in e:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening.index(stack.pop()) != closing.index(char):
                return "Invalid"
    return "Valid" if not stack else "Invalid"          

expr = input("Enter an expression: ")
print(f"Input: \n{expr}")
print(f"Output: \n{is_valid_expression(expr)}")
