def is_parentheses_balanced(expression):
    """
    Check if parentheses and brackets are properly balanced in an expression

    Args:
        expression (str): The input expression to check

    Returns:
        str: "Valid" if balanced, "Invalid" if not balanced
    """
    # Create an empty stack to keep track of opening brackets
    stack = []

    # Define matching pairs - each opening bracket maps to its closing bracket
    matching_brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    # Get all opening brackets for quick checking
    opening_brackets = set(matching_brackets.keys())  # {'(', '{', '['}
    # Get all closing brackets for quick checking
    closing_brackets = set(matching_brackets.values())  # {')', '}', ']'}

    # Iterate through each character in the expression
    for char in expression:
        # If current character is an opening bracket
        if char in opening_brackets:
            # Push it onto the stack to remember we need to find its match
            stack.append(char)

        # If current character is a closing bracket
        elif char in closing_brackets:
            # Check if we have any opening bracket waiting to be matched
            if not stack:
                # No opening bracket to match - this closing bracket is invalid
                return "Invalid"

            # Pop the most recent opening bracket from stack
            last_opening = stack.pop()

            # Check if the popped opening bracket matches the current closing bracket
            if matching_brackets[last_opening] != char:
                # Brackets don't match (e.g., we have '(' but found '}')
                return "Invalid"

        # If character is not a bracket, we ignore it (letters, numbers, operators, etc.)

    # After processing all characters, check if any opening brackets remain unmatched
    if stack:
        # Stack not empty means some opening brackets were never closed
        return "Invalid"
    else:
        # Stack is empty - all brackets were properly matched
        return "Valid"


# Test the function with various examples
def test_parentheses_checker():
    """Test function with multiple examples to verify correctness"""

    test_cases = [
        # Valid cases
        ("(4+(2+1))", "Valid"),           # Given example - should be Valid actually
        ("(a+b)", "Valid"),               # Simple parentheses
        ("{[()]}", "Valid"),              # Nested different brackets
        ("((()))", "Valid"),              # Multiple nested same brackets
        ("", "Valid"),                    # Empty string
        ("abc", "Valid"),                 # No brackets at all

        # Invalid cases
        ("(4+(2+1)", "Invalid"),          # Missing closing parenthesis
        (")", "Invalid"),                 # Closing without opening
        ("({)}", "Invalid"),              # Wrong order - parentheses inside braces
        ("(()", "Invalid"),               # Missing closing bracket
        ("())", "Invalid"),               # Extra closing bracket
    ]

    print("Testing Parentheses Checker:")
    print("-" * 40)

    for expression, expected in test_cases:
        result = is_parentheses_balanced(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expression}' -> {result} (expected: {expected})")


# Run the tests
if __name__ == "__main__":
    test_parentheses_checker()

    # Interactive testing
    print("\n" + "="*50)
    print("Interactive Testing:")
    print("Enter expressions to check (press Enter with empty input to quit)")

    while True:
        user_input = input("\nEnter expression: ").strip()
        if not user_input:
            break

        result = is_parentheses_balanced(user_input)
        print(f"Result: {result}")
