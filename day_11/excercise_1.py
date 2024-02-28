def safe_convert_to_int(value):
    try:
        result = int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to an integer.")
    else:
        print(f"Conversion successful: {result}")
        return result

safe_convert_to_int("123")  # Should succeed
safe_convert_to_int("abc")  # Should fail
