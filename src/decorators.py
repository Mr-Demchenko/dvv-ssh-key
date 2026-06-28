from datetime import datetime
from functools import wraps


def log(filename: str | None = None):
    """Декоратор записывает логи для запускаемой функции. Запись происходит в файл или в консоль."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_list = []
            time_begin = datetime.now()
            log_list.append(f'start {func.__name__} in {time_begin}')
            try:
                result = func(*args, **kwargs)
                log_list.append(f'Result of {func.__name__} in {datetime.now()} is {result}')
                return result
            except Exception as error:
                log_list.append(f'{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}.')
                raise
            finally:
                time_end = datetime.now()
                log_list.append(f'end {func.__name__} {time_end}')

                if filename is None:
                    for each_list in log_list:
                        print(each_list)
                else:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        for each_list in log_list:
                            log_file.write(f'{each_list} \n')

        return wrapper

    return decorator


@log()
def summ(a,r):
    return a+r


print(summ(3,5))