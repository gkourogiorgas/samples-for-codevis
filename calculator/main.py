from input_handler import InputHandler
from calculator import Calculator
from utils import print_welcome_message, print_goodbye_message


def run_calculator():
    """Main function to run the calculator"""
    calculator = Calculator()
    input_handler = InputHandler()

    print_welcome_message()

    while True:
        try:
            # Get user input
            numbers, operation = input_handler.process_input()

            # Perform calculation
            result = calculator.calculate(numbers, operation)

            # Display result
            calculator.display_result(result)

            # Ask if user wants to continue
            choice = input(
                "\nDo you want to perform another calculation? (y/n): "
            ).lower()
            if choice != "y":
                # Show calculation history before exiting
                calculator.show_history()
                break

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

    print_goodbye_message()


if __name__ == "__main__":
    run_calculator()
