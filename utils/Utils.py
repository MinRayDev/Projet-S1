def is_correct_number(number, minvalue, maxvalue):
    return number.isnumeric() and (minvalue <= int(number) <= maxvalue)

