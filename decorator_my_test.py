import time


def func1(z):
    def func2(x):
        return z*x
    return func2


res = func1(10)
res = func1(40)
print(res(20))


def return_cel_num(func):
    def wrapper(*args, **qwargs):
        result = func(*args, **qwargs)
        if isinstance(result, float):
            return round(result)
        elif isinstance(result, (list, tuple)):
            rounded = [round(x) if isinstance(x, float) else x for x in result]
            return type(result)(rounded)
    return wrapper


@return_cel_num
def ww():
    return [2.5, 5.1, 6.9]


print(ww())


def start_func(func):
    def wrapper(*args, **qwargs):
        for i in range(3):
            try:
                return func(*args, **qwargs)
            except Exception:
                time.sleep(3)
        raise Exception('Ничо не понимаю')
    return wrapper


def funcSS(func):
    def wrapper(*args, **qwargs):
        result = func(*args, **qwargs)
        if type(result) in (list, tuple):
            for i in result:
                yield i
            else:
                yield result
    return wrapper


def func_text(func):
    def wrapper(*args, **qwargs):
        result = func(*args, **qwargs)
        if isinstance(result, str):
            list_res = result.split()
            return " ".join(f'{x[0:8]}.' if len(x) > 8 else x for x in list_res)
        else:
            return result
    return wrapper


def replace(func):
    def wrapper(*args, **qwargs):
        result = func(*args, **qwargs)
        if isinstance(result, str):
            new_str = ""
            for i in result:
                if i == "!":
                    new_str = new_str + "!!!"
                else:
                    new_str = new_str + i
            return new_str
        else:
            return result

    return wrapper
