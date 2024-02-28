import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')

def validate_positive_integer(value):
    try:
        value = int(value)
        assert value > 0, "Value must be positive."
    except ValueError:
        logging.error(f"Invalid input: '{value}' is not an integer.")
    except AssertionError as error:
        logging.error(f"Validation failed: {error}")

validate_positive_integer("5")  # Valid input
validate_positive_integer("-3")  # Invalid: not positive
validate_positive_integer("abc")  # Invalid: not an integer
