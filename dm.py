def calculate(number_1, number_2):
    """
    This function performs calculations on two provided numbers
    and handles division by zero. The calculations to do are:
        . Sum
        . Difference
        . Product
        . Quotient
    
    Args:
        number_1: The first number
        number_2: The second number

    Returns:
        A dictionary containing the calculation results:
            sum: the sum of number_1 and number_2
            difference: the difference of number_1 and number_2
            product: the product of number_1 and number_2
            quotient: the quotient of number_1 and number_2 (or a message if division by zero)
    """

    try:
        # Validate input types
        if not isinstance(number_1, (int, float) or not isinstance(number_2, (int, float))):
            raise ValueError("Invalid input: Please enter numbers only")
        
        # Convert inputs to floats for calculation
        number_1 = float(number_1)
        number_2 = float(number_2)

        sum_result = number_1 + number_2
        difference_result = number_1 - number_2
        product_result = number_1 * number_2

        if number_2 == 0:
            quotient_result = "Division by zero is not allowed!"
        else:
            quotient_result = number_1 / number_2    

        return dict(sum=sum_result, difference=difference_result, product=product_result, quotient=quotient_result)
    except (ValueError, ZeroDivisionError) as e:
        if isinstance(e, ValueError):
             print(f"Error: {e} (Invalid input format)")
        else:
            print(f"Error: {e}")
        return None