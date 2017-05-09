# l=[('bob',56),('adam',93),('bart',66),('lisa',88)]
# def by_name(t):
#     return t
# l1=sorted(l,key=by_name)#####通过名字来排序
#
# def by_score(t):####通过分数来排序
#     return t[:][1]
# l2=sorted(l,key=by_score,reverse=True)

# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum
# f=lazy_sum(1,34,5,2)####这样调用不会直接进行计算
# print(f())#####调用一下输出才会计算

def log(func):#####装饰器
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2015-3-25')

now()

