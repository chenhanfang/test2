# import numpy
# x=numpy.ones(3)
# y=numpy.ones((3,4))
# m=numpy.eye(3)
# n=numpy.eye((3,4))

#
# #coding=utf-8
# import math
# def quadratic(a,b,c):
#     for n in (a,b,c):
#         if not isinstance(n,(float,int)):
#             raise TypeError ('参数必须是数字！')
#     if a == 0:
#          print('a不能为0！')
#     elif b*b-4*a*c<0:
#         print('无解')
#     else:
#         x1=float((-b+math.sqrt(b*b-4*a*c))/(2*a))
#         x2=float((-b-math.sqrt(b*b-4*a*c))/(2*a))
#         print('一元二次方程的根是：（%.2f,%.2f)'%(x1,x2))
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# quadratic(a,b,c)
#
#
# def cals(*numbers):####可以传参数或者不传
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
#
# def fact(n):#####递归函数，递归调用的次数过多，会导致栈溢出
#     if n==1:
#         return 1
#     return n*fact(n-1)

# def fact1(n):#######尾递归优化,还是会导致栈溢出
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num -1,num*product)
# print(fact1(100))

def move(n,a,b,c):#####汉诺塔，虽然不是很懂
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)

move(3,'a','b','c')

l=[]
n=1
while n<=99:
    l.append(n)
    n=n+2

print()
