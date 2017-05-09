# def fibonacci(n,cache=None):
#     if cache is None:####增加缓存字典
#         cache={}
#     if n in cache:
#         return cache[n]
#     if n <= 1:
#         return 1
#     cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)####如果缓存没有，就把他增加到缓存中
#     return cache[n]
#     # return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(50))

#####装饰器方法
from functools import wraps
def add_cache(func):
    '''
    This add_cache
    '''
    cache = {}
    @wraps(func)
    def wrap(*args):
        '''
        This wrap
        '''
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
@add_cache###装饰器
def fibonacci1(n):
    '''
    This fibonacci1
    '''
    if n <= 1:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)
# fibonacci=add_cache(fibonacci1)
print(fibonacci1(50))
print(fibonacci1.__name__)
print(fibonacci1.__doc__)
