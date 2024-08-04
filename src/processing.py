def filter_by_state(operations_list: list, state='EXECUTED') -> list:
    """Возвращает список словарей, ключ которых соответствует указанному значению"""
    res = []
    for operation in operations_list:
        for k, v in operation.items():
            if v == state:
                res.append(operation)
    return res

def sort_by_date(operations_list: list, des_order=True):
    """Сортирует список словарей по полю 'дата' по убыванию или по возрастанию"""
    sorted_list = sorted(operations_list, key=lambda k: k['date'], reverse=des_order)
    return sorted_list
