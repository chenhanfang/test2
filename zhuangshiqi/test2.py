# def func_100(val):
#     passline=60
#     if val>=passline:
#         print('%d pass'%val)
#     else:
#         print('failed')
# def func_150(val):
#     passline=90
#     if val>=passline:
#         print('%d pass'%val)
#     else:
#         print('failed')

# 闭包：1.封装，2.代码复用
def set_passline(passline):
    def cmp(val):
        if val>=passline:
            print('%d pass'%val)
        else:
            print('failed')
    return cmp

f_100=set_passline(60)
f_150=set_passline(90)
print(f_100)
print(f_100 .__closure__ )
f_100(80)
f_150(68)