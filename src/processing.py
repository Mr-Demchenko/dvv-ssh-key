def filter_by_state(list_d: list[dict], state='EXECUTED'):
    result_list = list()
    for element in list_d:
        for key, value in element.items():
            if (key == 'state') & (value == state):
                result_list.append(element)
    return result_list