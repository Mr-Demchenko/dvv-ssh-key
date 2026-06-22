from functools import wraps


def log(filename: str | None = None):
    """Функция записывает логи в файл или в консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as error:
                message = (
                    f"{func.__name__} error: {type(error).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: str):
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{message}\n")
    else:
        print(message)
