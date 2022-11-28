def is_correct_number(number: str, min_value: int, max_value: int) -> bool:
    return number.isnumeric() and (min_value <= int(number) <= max_value)
