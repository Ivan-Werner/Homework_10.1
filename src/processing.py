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


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                          ))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                       ))
