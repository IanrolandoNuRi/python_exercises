import pytest 
from faker import Faker


import function as fn


def test_add_funct():
    fake = Faker()

    first_val = fake.pyint(0, 10)
    second_val = fake.pyint(0, 10)

    result = fn.add_function(first_value = first_val, second_value = second_val)
    result_expected = first_val + second_val
    print(f"result + ' equals '+ result_expected")
    assert result == result_expected


@pytest.mark.parametrize(
    "test_input",
    [5,27],
)
def test_should_return_cold_or_hot_acording_input_temperature(test_input):
    
    fake= Faker()

    random_temperature = test_input

    result = fn.cold_or_hot_temperature(random_temperature = random_temperature)

    expected_result = "hot" if random_temperature > 20 else "cold"

    assert result == expected_result