def is_correct_number(size, minvalue, maxvalue):
    return size.isnumeric() and (minvalue <= int(size) <= maxvalue)

