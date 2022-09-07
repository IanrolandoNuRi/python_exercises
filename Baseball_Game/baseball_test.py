from unittest import mock
import pytest
# from faker import Faker

import baseball as bsb

# Validatidate sum_two_array_elements happy path
# @pytest.mark.parametrize(
#     "score_array_error",
#     ['C','D'],
# )
# def test_should_show_error_if_exist_no_number_element_previous(score_array_error):

#     expected_result = "Sorry, we cannot duplicate or remove the element, please use at least one number in the array"
#     score_array = score_array_error

#     result = bsb.final_result(score_array)

#     assert result == expected_result

# @pytest.mark.parametrize(
#     "score_array_error",
#     ['+',['+', 2], [2 ,'+'], [2, '+', 2, 3]],
# )
# def test_should_show_error_if_not_found_two_number_element_previous(score_array_error):

#     expected_result = "Sorry, we cannot sum the elements, please use at least two numbers in the array"
#     score_array = score_array_error

#     result = bsb.final_result(score_array)

#     assert result == expected_result


# def test_should_return_the_sum_of_all_the_scores():
    
#     expected_result = 30
#     score_game=[5, 2, 'C', 'D', '+']
#     # iterate_function = mock._iterate_given_board()
#     result = bsb.final_result(score_game)

#     # iterate_function.called_once()
#     assert result == expected_result


def test_should_return_list_with_last_item_added():
    
    expected_result = [1, 2, 3]
    result = [1, 2]
    result = bsb._add_element_into_given_array(result, 3)
    assert result == expected_result


def test_should_return_list_with_last_item_duplicate():
    
    expected_result = [1, 2, 3, 6]
    result = [1, 2, 3]
    result = bsb._duplicate_previous_score(result)
    assert result == expected_result


def test_should_return_list_without_last_item_():
    
    expected_result = [1, 2]
    result = [1, 2, 3]
    result = bsb._remove_element_from_given_array(result)
    assert result == expected_result


def test_should_return_list_with_sum_last_two_items():
    
    expected_result = [1, 2, 3, 5]
    result = [1, 2, 3]
    result = bsb._sum_previous_two_elements_from_given_array(result)
    assert result == expected_result


@pytest.mark.parametrize(
    "array_input,operation,expected_result",
    [
        ([9, 3],'D',[9, 3, 6]),
        ([4, 7],'C',[4]),
        ([8, 4],'+',[8, 4, 12])
    ],
)
def test_should_return_list_with_operation_is_according(array_input, operation, expected_result):
    expected_result = expected_result
    score_game = array_input
    result = bsb._handler_item_input(score_game,operation)

    assert result == expected_result