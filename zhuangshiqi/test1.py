#coding=utf-8
passline=60
def func(val):
    print('%x'%id(val))
    if val>=passline:
        print('pass')
    else:
        print('failed')
    def in_func():
        print(val)
    in_func()
    return in_func

f=func(89)
f()#in_func
print(f.__closure__)#####与id(val)相同的值