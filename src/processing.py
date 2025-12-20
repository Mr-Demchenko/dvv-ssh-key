def filter_by_state(list_of_dict: list[dict], state='EXECUTED') -> list:
    result_list = list()
    for element in list_of_dict:
        for key, value in element.items():
            if (key == 'state') & (value == state):
                result_list.append(element)
    return result_list


def sort_by_date(list_of_dict: list[dict], need_reverse=False) -> list:
    return sorted(list_of_dict, key=lambda s_date: s_date['date'], reverse=need_reverse)