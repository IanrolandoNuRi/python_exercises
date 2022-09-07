import constants


def _handler_item_input(final_game_score : list, element_from_gaming_score: chr) -> int:
    error_found = constants.not_errors_found
    try: 
        if(isinstance(int(element_from_gaming_score), int)): 
            final_game_score = _add_element_into_given_array(final_game_score, int(element_from_gaming_score))
    except:
        if element_from_gaming_score == constants.remove_previous_score: 
            if _validate_elements_from_given_array(final_game_score, 1) == True: final_game_score = _remove_element_from_given_array(final_game_score) 
            # else: error_found = constants.error_found_1
        if element_from_gaming_score == constants.double_previous_score: 
            if _validate_elements_from_given_array(final_game_score, 1) == True: final_game_score = _duplicate_previous_score(final_game_score)
            # else: error_found = constants.error_found_1
        if element_from_gaming_score == constants.sum_previous_two_scores: 
            if _validate_elements_from_given_array(final_game_score, 2) == True: final_game_score = _sum_previous_two_elements_from_given_array(final_game_score)
            # else: error_found = constants.error_found_2
        return final_game_score 

def _add_element_into_given_array(final_game_score : list, element_from_gaming_score: chr) -> list:
    list_with_item_added = [*final_game_score]
    list_with_item_added.append(element_from_gaming_score)
    return list_with_item_added

def _duplicate_previous_score(final_game_score : list) -> list:
    list_with_item_duplicated = [*final_game_score]
    return _add_element_into_given_array(
        list_with_item_duplicated,
        list_with_item_duplicated[len(list_with_item_duplicated)-1] * 2
    )

def _remove_element_from_given_array(final_game_score : list) -> list:
    list_without_last_item = [*final_game_score]
    del(list_without_last_item[len(list_without_last_item)-1])
    return list_without_last_item

def _sum_previous_two_elements_from_given_array(final_game_score : list) -> list:
    list_with_sum_two_last_items = [*final_game_score]
    last_item : int = list_with_sum_two_last_items[len(list_with_sum_two_last_items)-1]
    previous_last_item : int = list_with_sum_two_last_items[len(list_with_sum_two_last_items)-2]
    return _add_element_into_given_array(list_with_sum_two_last_items, previous_last_item+last_item)


def _validate_elements_from_given_array(final_game_score : list, min_length_array_size : int) -> bool: 
    is_valid = True if len(final_game_score) >= min_length_array_size else False 
    print(final_game_score)
    # return is_valid
    return True


def _sum_final_game_board(final_game_board: list)  -> int:
    total_score_game = 0
    for score in final_game_board: total_score_game = total_score_game + score
    return total_score_game


def _iterate_given_board(game_score_board: list) -> list or int:
    final_game_score = []
    for score in game_score_board:
        if _handler_item_input(final_game_score, score):
            final_game_score= _handler_item_input(final_game_score, score)
            return(_handler_item_input(final_game_score, score))

    return final_game_score


def final_result(game_score_board : list):
    final_game_board =_iterate_given_board(game_score_board)
    if final_game_board == constants.error_found_1: return constants.duplicate_or_remove_error 
    if final_game_board == constants.error_found_2: return constants.sum_error
    return _sum_final_game_board(final_game_board)

# def _find_last_integer_element_from_given_array(final_game_score : list, item_until_iterate_find_it = None):
#     if item_until_iterate_find_it is None:
#         for index, last_item in enumerate(final_game_score[::-1]):
#             if(isinstance(last_item, int)):
#                 print(index)
#                 return(last_item)