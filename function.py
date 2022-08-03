def add_function(first_value : int, second_value : int) -> int:
    add = first_value + second_value if _validate_value(first_value) == True and _validate_value(second_value) == True else False
    return add


def _validate_value(number_to_validate : int) -> bool :
    return( True if number_to_validate < 11 and number_to_validate >= 0 else False)


def cold_or_hot_temperature(random_temperature: int):
    temp = "hot" if random_temperature > 20 else "cold"
    return temp
