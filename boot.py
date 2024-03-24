from dm import calculate
import re
import logging

# Configure logging (optional)
logging.basicConfig(filename='calculator.log', level=logging.DEBUG)  # Save logs to a file

def get_user_input(prompt):
    """
    Prompts the user for input and returns the validated numeric value.

    Args:
        prompt: The message to display to the user.

    Returns:
        The validated numeric input as a float, or None if invalid. 
    """

    while True:
        value = input(prompt)
        # Improved validation using regular expressions
        if not value.strip() or not re.match(r"^\d+\.?\d*$", value):
            logging.error("Invalid input received from user.")  # Log error message
            print("Invalid input. Please enter a number (including decimals).")
            continue

        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number (including decimals).")

def main():
    """
    The main function for user interaction and calculation execution.
    """
    number_1 = get_user_input("Enter your first number: ")
    number_2 = get_user_input("Enter your second number: ")

    if number_1 is None or number_2 is None:
        print("Error: Invalid input. Please try again!")
        return

    results = calculate(number_1, number_2)

    if results:
        print("Sum:", results["sum"])
        print("Difference:", results["difference"])
        print("Product:", results["product"])
        print("Quotient:", results["quotient"])
    else:
        print("An error occurred during calculations.")

if __name__ == "__main__":
    logging.info("Starting calculator application.")  # Log informational message
    main()
