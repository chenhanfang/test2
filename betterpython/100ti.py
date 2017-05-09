# for i in range(1,5):#####1,2,3,4组成的无重复的三位数字
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i!=j)and(i!=k)and(j!=k):
#                 print(i,j,k)

# import math######一个整数加上100或者268都是完全平方
# for i in range(100000):
#     x=int(math.sqrt(i+100))
#     y=int(math.sqrt(i+286))
#     if (x*x == i+100)and(y*y == i+268):
#         print(i)

# year=int(input('请输入年份：'))#####输入年份时间，判断是那年的第几天
# month=int(input('请输入月份：'))
# data=int(input('请输入日期：'))
# months=(0,31,59,90,120,151,181,212,243,273,304,334)
# if 0<=month<=12:
#     sum=months[month-1]
# else:
#     print('data error!')
# sum+=data
# leap=0
# if(year%400==0)or(year%4==0)and(year%100!=0):
#     leap=1
# if(leap==1)and(month>2):
#     sum+=1
# print('it is the %sth day.'%sum)

# l=[]#####输入三个数字，进行排序
# for i in range(3):
#     x=int(input('请输入数字：'))
#     l.append(x)
# l.sort()####将数组进行排序
# print(l)

# print('hello python world!\n')###打印c型
# print('*'*10)
# for i in range(5):
#     print('* ')
# print('*'*10)
# # print('*\n'*6)

# a=176
# b=218
# print(chr(b),chr(a),chr(a),chr(a),chr(b))
# print(chr(a),chr(b),chr(a),chr(b),chr(a))
# print(chr(a),chr(a),chr(b),chr(a),chr(a))
# print(chr(a),chr(b),chr(a),chr(b),chr(a))
# print(chr(b),chr(a),chr(a),chr(a),chr(b))

# import sys#####打印楼梯
# sys.stdout.write(chr(1))
# sys.stdout.write(chr(1))
# print("")
#
# for i in range(1,11):
#     for j in range(1,i):
#         sys.stdout.write(chr(219))
#         sys.stdout.write(chr(219))
#     print("")

####九九乘法表的打印
# ##1.
# for i in range(1,10):
#     for j in range(1,10):
#         result=i*j
#         print('%s*%s=%-3d'%(i,j,result),end=' ')
#     print(" ")
# print('\n')
#
# ###2.
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%-2d'%(i,j,i*j),end=' ')
#     print('')
# print('\n')
#
# ###3.
# for i in range(1,10):
#     for j in range(i,10):
#         print('%s*%s=%-2d'%(i,j,i*j),end=' ')
#     print(' ')

####1,1,2,3,5,8,....数列输出
# f1=1
# f2=1
# for i in range(1,21):
#     print('%12d,%12d'%(f1,f2),end=',')
#     if (i%2) == 0:
#         print(' ')
#     f1=f1+f2
#     f2=f1+f2


#####需找素数
# count=0
# for i in range(101,201):
#     for j in range(2,i):
#         if i%j == 0:
#            break
#     else:
#         print('%-4d'%i)
#         count = count + 1
# print('the total is %s'%count)

#####水仙花数
# for i in range(100,1001):
#     x = i % 10
#     y = int(i / 10 % 10)
#     z = int(i / 100)
#     # print('%s,%s,%s'%(x,y,z))
#     if i == x**3 + y**3 + z**3:
#         print('%5d'%i)


# #####将一个正整数分解质因数
# from sys import stdout
# n=int(input('input number:\n'))
# print('n= %d'%n)
# for i in range(2,n+1):
#     while n != i:
#         if n % i ==0:
#             stdout.write(str(i))
#             stdout.write("*")
#             n=n/i
#         else:
#             break
# print("%d"%n)

#######统计输入的字符串中中英文字母，空格，数字和其他字符的个数
# import string
# s=input('input a string:\n')
# letters=0
# space=0
# digit=0
# others=0
# for c in s:
#     if c.isalpha():
#         letters +=1
#     elif c.isspace():
#         space +=1
#     elif c.isdigit():
#         digit +=1
#     else:
#         others +=1
# print('char=%s,space=%d,digit=%d,others=%d'%(letters,space,digit,others))


# ####求s=a+aa+aaa+....+aa...a
# s=0
# l=[]
# sum=0
# n=int(input('n=\n'))
# a=int(input('a=\n'))
# for count in range(n):
#     s=s+a
#     a=a*10
#     l.append(s)
#     print(s)
# for i in range(0,n):
#     sum=sum+l[i]
# print('sum=%s'%sum)

###找到完数，例如6=1+2+3
from sys import stdout
for n in range(2,1001):
    k=[]
    z=-1
    s=n
    for i in range(1,n):
        if n%i==0:
            z+=1
            s-=i
            k.append(i)
    if s==0:
        print(n)
        for i in range(z):
            stdout.write(str(k[i]))
            stdout.write(" ")
        print(k[z])



