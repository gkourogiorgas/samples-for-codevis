from utils import format_result


class Calculator:
    """Core calculator logic"""

    def __init__(self):
        self.history = []

    def calculate(self, numbers, operation):
        """Perform calculation and store in history"""
        try:
            result = operation.execute(numbers)
            calculation = {
                "numbers": numbers,
                "operation": operation.name,
                "result": result,
            }
            self.history.append(calculation)
            return result
        except Exception as e:
            print(f"Error during calculation: {e}")
            return None

    def display_result(self, result):
        """Display the calculation result"""
        if result is not None:
            formatted_result = format_result(result)
            print(f"Result: {formatted_result}")

    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations performed yet.")
            return

        print("\nCalculation History:")
        for i, calc in enumerate(self.history, 1):
            numbers_str = ", ".join(str(num) for num in calc["numbers"])
            print(f"{i}. {calc['operation']} of [{numbers_str}] = {calc['result']}")
