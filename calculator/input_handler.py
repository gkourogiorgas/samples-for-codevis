from operations import Addition, Multiplication, Power, Average, Maximum, Minimum


class InputHandler:
    """Handles user input for the calculator"""

    def __init__(self):
        self.operations = {
            "add": Addition(),
            "multiply": Multiplication(),
            "power": Power(),
            "average": Average(),
            "max": Maximum(),
            "min": Minimum(),
        }

    def get_numbers(self):
        """Get a list of numbers from the user"""
        while True:
            try:
                input_str = input("Enter numbers separated by spaces: ")
                numbers = [float(num) for num in input_str.split()]
                if not numbers:
                    print("Please enter at least one number.")
                    continue
                return numbers
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def get_operation(self):
        """Get the desired operation from the user"""
        available_ops = ", ".join(self.operations.keys())

        while True:
            operation_name = input(f"Enter operation ({available_ops}): ").lower()
            if operation_name in self.operations:
                return self.operations[operation_name]
            print(f"Invalid operation. Available operations: {available_ops}")

    def process_input(self):
        """Process user input and return numbers and operation"""
        numbers = self.get_numbers()
        operation = self.get_operation()
        return numbers, operation
