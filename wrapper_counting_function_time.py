import time


def wrapper_time(func):
    def count_time(*args, **kwargs):
        start = time.time()
        v = func(*args, **kwargs)
        stop = time.time()
        print(f'Function {func.__name__} executed in {stop - start}')
        return v
    return count_time


@wrapper_time
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(4))
