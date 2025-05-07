import time
from inspect import getfullargspec
from functools import wraps

def cached(_func = None, *, max_size = None, seconds = None):
    def decorator(func):
        def old_cleaner():
            if lifetime is None: return
            current_timestamp = time.time()
            for key in list(cache.keys()):
                if current_timestamp - cache[key][0] > lifetime:
                    del cache[key]

        def push_to_cache(args_assembled, func_results):
            if cache_size is not None and len(cache) >= cache_size:
                while len(cache) >= cache_size:
                    oldest_key, oldest_value = None, None
                    for key, value in cache.items():
                        if oldest_key is None or value[0] < oldest_value[0]:
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
            if ((cache_size is not None and cache_size == 0)
                    or (lifetime is not None and lifetime == 0)):
                return func(*args, **kwargs)
            old_cleaner()
            args_assembled = args_assembly(*args, **kwargs)
            if args_assembled not in cache:
                push_to_cache(args_assembled, func(*args, **kwargs))
            return cache[args_assembled][1]
        keys = getfullargspec(func).args
        lifetime = seconds if type(seconds) == int and seconds >= 0 else None
        cache_size = max_size if type(max_size) == int and max_size >= 0 else None
        cache = {} # { <func_arguments>: (<timestamp>, <func_result>), ... }
        return wrapper
    if _func is None: return decorator
    else: return decorator(_func)

@cached(max_size=10, seconds=0)
def slow_function(x, message = None):
    print(f"Вычисляю для {x}... {message}")
    return x ** 2

@cached(max_size=2, seconds=20)
def generator(x, message = None):
    print(f"Генерирую для {x}... {message}")
    return x, message

print(generator(5, "good"))
print(generator(5, "good"))
print(slow_function(4))
print(slow_function(4))
print(slow_function(3, "hello"))
print(generator(6, "hi"))
print(slow_function(2, "hello"))
print(slow_function(3, "hi"))
print(generator(6))
print(generator(6))
time.sleep(15)
print(slow_function(2, "hello"))
print(slow_function(3, "hi"))
print(generator(6))
