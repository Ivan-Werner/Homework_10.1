from functools import wraps


def log(filename=None):
    """Декоратор, осуществляющий логирование функции и выводящий логи в конслоль или файл"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"Function start working.\nFunction finish working.\n"
            except Exception as e:
                result = f"Error. Arguments has wrong type. Arguments: {args}, {kwargs}"
                log_message = f"Error: {e}. Arguments: {args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result
        return wrapper
    return decorator

@log()
@log(filename="mylog.txt")
def my_function(x, y):
    """Функция, складывающая два числа"""
    return x + y

print(my_function(1, 2))






