def filter_by_state(operations_list: list, state='EXECUTED') -> list:
    """Возвращает список словарей, ключ которых соответствует указанному значению"""
    res = []
    for operation in operations_list:
        for k, v in operation.items():
            if v == state:
                res.append(operation)
    return