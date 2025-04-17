def format_result(result):
    """Format the result for display"""
    # If result is an integer, display as integer
    if isinstance(result, float) and result.is_integer():
        return int(result)

    # For floats, limit to 4 decimal places if needed
    if isinstance(result, float):
        # Check if it has more than 4 decimal places
        if abs(result - round(result, 4)) < 1e-10:
            return round(result, 4)

    return result


def print_welcome_message():
    """Print welcome message for the calculator"""
    print("=" * 50)
    print("Welcome to the Mathematical Operations Calculator")
    print("=" * 50)
    print("This calculator can perform various operations on a list of numbers.")
    print("=" * 50)


def print_goodbye_message():
    """Print goodbye message"""
    print("\n" + "=" * 50)
    print("Thank you for using the Mathematical Operations Calculator!")
    print("=" * 50)
