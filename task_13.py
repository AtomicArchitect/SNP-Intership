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
                if len(keys) == 0: result.append(arg)
                else: result[idx] = arg
            return ''.join(map(str, result))

        @wraps(func)
        def wrapper(*args, **kwargs):
            if ((cache_size is not None and cache_size == 0)
                    or (lifetime is not None and lifetime == 0)):
                return func(*args, **kwargs)
            args_assembled = args_assembly(*args, **kwargs)
            if args_assembled not in cache:
                push_to_cache(args_assembled, func(*args, **kwargs))
            result = cache[args_assembled][1]
            old_cleaner()
            return result
        keys = getfullargspec(func).args
        lifetime = seconds if type(seconds) == int and seconds >= 0 else None
        cache_size = max_size if type(max_size) == int and max_size >= 0 else None
        cache = {} # { <func_arguments>: (<timestamp>, <func_result>), ... }
        return wrapper
    if _func is None: return decorator
    else: return decorator(_func)

@cached(max_size=10, seconds=10)
def slow_function(*args, **kwargs):
    print("Вычисляю для {} {}".format(args, kwargs))
    return len(args)

print(slow_function(None))
print(slow_function(None))
print(slow_function(None))
time.sleep(15)
print("sleep end")
print(slow_function(None))
print(slow_function(None))
