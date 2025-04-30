import time
from inspect import getfullargspec
from functools import wraps

def cached(_func = None, *, max_size = None, seconds = None):
    def decorator(func):
        def cache_cleaner():
            if max_size is None and seconds is None: return
            current_timestamp = time.time()
            for key in list(cache.keys()):
                if current_timestamp - cache[key][0] > lifetime:
                    del cache[key]

        def push_to_cache(args_assembled, func_results):
            if cache_size is not None and len(cache) >= cache_size:
                oldest_key, oldest_value = None, None
                for key, value in cache.items():
                    if oldest_key is None:
                        oldest_key = key
                        oldest_value = value
                    elif value[0] < oldest_value[0]:
                        oldest_key = key
                        oldest_value = value
                del cache[oldest_key]
            cache[args_assembled] = (time.time(), func_results)

        def args_assembly(*args, **kwargs):
            result = []
            for key in keys:
                if key in kwargs: result.append(kwargs[key])
                else: result.append(None)
            for idx, arg in enumerate(args):
                result[idx] = arg
            return ''.join(map(str, result))

        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_cleaner()
            args_assembled = args_assembly(*args, **kwargs)
            if args_assembled in cache:
                return cache[args_assembled][1]
            else:
                push_to_cache(args_assembled, func(*args, **kwargs))
                return cache[args_assembled][1]
        keys = getfullargspec(func).args
        lifetime = seconds if type(seconds) == int and seconds > 0 else None
        cache_size = max_size if type(max_size) == int and max_size > 0 else None
        cache = {} # { <func_arguments>: (<timestamp>, <func_result>), ... }
        return wrapper
    if _func is None: return decorator
    else: return decorator(_func)

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
print(slow_function(3)) # Вывод: "Вычисляю для 3..." → 9
print(slow_function(3)) # Из кеша
print(slow_function(4)) # Вывод: "Вычисляю для 4..." → 16
print(slow_function(4)) # Из кеша
print(slow_function(5)) # Вывод: "Вычисляю для 5..." → 25
print(slow_function(5)) # Из кеша
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
print(slow_function(2)) # Из кеша
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
print(slow_function(3)) # Вывод: "Вычисляю для 3..." → 9
