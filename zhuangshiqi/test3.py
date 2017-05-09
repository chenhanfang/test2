# 闭包中引用函数
# def my_sum(*arg):
#     return sum(arg)
# def my_average(*arg):
#     return sum(arg)/len(arg)

def dec(func):
    def in_dec(*arg):
        if len(arg)==0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec
# 装饰器
@dec
def my_sum(*arg):
    return sum(arg)
@dec
def my_average(*arg):
    return sum(arg)/len(arg)

# 作用和装饰器相同
# my_sum=dec(my_sum)
# my_average=dec(my_average)

print(my_sum(1,2,3,2))
print(my_average(5,38,4,5))