# class Dog():
#     def __init__(self,name,age):###初始化属性
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(self.name.title()+' is now sitting.')
#     def roll_over(self):
#         print(self.name.title() + ' rolled over!')
#
# my_dog=Dog('while',6)###实例化类
# my_dog.sit()
# my_dog.roll_over()
# print(my_dog.name.title() )

# class Restaurant():######餐馆类，衍生冰淇淋店
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#         self.number_served=10
#     def describe_restaurant(self):
#         print(self.name.title()+' is a '+self.type)
#     def open_restaurant(self):
#         print(self.name.title()+' is now opening!')
#     def set_number_served(self,numbers):###设置餐馆现有的人数
#         self.number_served=numbers
#     def increment_number_served(self,in_number):####判断即将接待的人数
#         if self.number_served+in_number < 100:
#             self.number_served += in_number
#             print('welcome to our restaurant!')
#         else:
#             print('there do not have evenogh tables!')
#     def read_number(self):#####获取打印就餐人数
#         print('there are '+str(self.number_served )+' persons!')
#
# class IceCreamStand(Restaurant):
#     def __init__(self,name,type):
#         super().__init__(name,type)#####继承时不要写self
#         self.flavors='caomei'
# restaurant=Restaurant ('xinbailu','zhongcan')
# restaurant.describe_restaurant()
# restaurant.read_number()
# restaurant.set_number_served(20)
# restaurant.read_number()
# restaurant.increment_number_served(100)
# restaurant.read_number()
# restaurant.increment_number_served(30)
# restaurant.read_number()
# restaurant.open_restaurant()
# restaurant1=Restaurant('bishengke','xican')
# restaurant1.describe_restaurant()
# ice=IceCreamStand('HH','FEK')
# print(ice.name+'xxx '+ice.type+'yyy is '+ice.flavors )


# class Car():#####汽车类，衍生电动车
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name=str(self.year)+' '+self.make+' '+self.model
#         return long_name.title()
#     def read_odometer(self):
#         print('this car has '+str(self.odometer_reading)+' miles on it.')
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading=mileage
#         else:
#             print('you can not roll back an odometer!')
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
#     def fill_gas_tank(self,gas):
#         self.gas=gas
#
# class Battery():
#     def __init__(self,battery_size=70):
#         self.battery_size=battery_size
#     def describe_battery(self):
#         print('this car has a '+str(self.battery_size)+'-kwh battery.')
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = 'this car can go approximately '+str(range)
#         message += ' miles on a full charge.'
#         print(message)
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size=85
#
# class ElectricCar(Car):####car的子类
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         # self.battery_size=70
#         self.battery=Battery()
#     def describe_battery(self):
#         print('this car has a '+str(self.battery_size)+'-kwh battery.')
#     def fill_gas_tank(self):
#         print('this car does not need a gas tank!')

# my_new_car=Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(-12)
# my_new_car.read_odometer()
# my_new_car.update_odometer(200)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(200)
# my_new_car.read_odometer()
# my_electri_tesla=ElectricCar ('tesla','models',2017)
# print(my_electri_tesla .get_descriptive_name())
# my_electri_tesla.battery.describe_battery()####调用battery类中的方法
# my_electri_tesla.battery.get_range()
# my_electri_tesla.fill_gas_tank()
# my_el_tesla=ElectricCar('tesla','models',2017)
# my_el_tesla.battery.get_range()
# my_el_tesla.battery.upgrade_battery()
# my_el_tesla.battery.get_range()



# from random import randint
# # x=randint(1,6)
# # print(x)
# class Die():
#     def __init__(self,side):
#         self.side=side
#         side=int(side)
#     def roll_die(self,a):#####摇不同面数骰子，并设置摇骰子的次数
#         if isinstance(a,int):
#             for i in range(a):
#                 x = randint(1, self.side)
#                 print(x)
#         else:
#             print('a must be int!')
#
# die=Die(10)
# die.roll_die(6)
# die2=Die(20)
# die2.roll_die(5)

# with open('hhh') as file_object:#####打开文件
#     # contents=file_object.read()#####读取文件内容
#     # print(contents.rstrip())####rstrip()去除末尾的空格
#     for line in file_object:#####分行读取文件
#         print(line.rstrip())


# filename='hhh'
# with open(filename) as file_object:
#     lines=file_object.readlines()
# pi_string=''
# for line in lines:#####分行读取赋值之后获取长度
#     # pi_string += line.rstrip()#####不删除左边的空格
#     pi_string += line.strip()#####删除左边的空格
# # print(pi_string)
# # print(len(pi_string))
# birthday=input('enter your birthday,in the form mmddyy:')
# if birthday in pi_string:
#     print('your birthday appears in the first million digits of pi!')
# else:
#     print('your birthday does not appear in the first million digits of pi.')


# message='i really like dogs'
# print(message.replace('dog','cat'))

# filename='progranmming.txt'######写入文件
# with open(filename,'w') as file_object:
#     file_object.write('i love programing.\n')
#     file_object.write('i love creating new games.\n')


# filename1='guest.txt'
#         # file_object .write('what is your name?\n')
# active=True
# while active:
#     name=input('what is you name?')
#     if name != 'quit':
#         with open(filename1, 'a')as file_object:#######a不覆盖之前的输入，w覆盖之前的输入
#             print('hello,%s' % name)
#             file_object.write('what is your name?\n'+name+'\n')
#     else:
#         active = False

# try:#######try-excep异常处理
#     print(5/0)
# except ZeroDivisionError:
#     print('you can not divide by zero')

# print('give me two numbers,and i will divide them.')
# print('enter q to quit.')
# while True:
#     first_number=input('\nfirst number:')
#     if first_number == 'q':
#         break
#     second_number=input('\nsecond number:')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print('you can not divide by 0!')
#     else:
#         print(answer)


# title='alice in wonderland'
# print(title.split())#######分析文本


# def count_words(filename):######定义函数操作
#     try:
#         with open(filename) as f_obj:
#             contents=f_obj.read()
#     except FileNotFoundError:
#         msg='sorry,the file'+filename+'does not exist.'
#         # pass######执行失败不会返回结果
#     else:
#         words=contents.split()
#         num_words=len(words)
#         print('the file '+filename+' has about '+str(num_words)+' words')
# filename='guest.txt'
# count_words(filename)

# while True:#######练习
#     try:
#         number1=input('please input first number:')
#         if number1== 'q':
#             break
#         number2=input('pleasr input second number:')
#         if number2 == 'q':
#             break
#         add=int(number1) + int(number2)
#         print(add)
#     except ValueError:
#         print('you can not input wenzi')


# import json
# numbers=[2,3,34,5,44,31]
# filename = 'numbers.json'#######创建json文件
# with open(filename,'w')as f_obj:
#     json.dump(numbers,f_obj)#####写入json文件中,dump存储到文件中
# #

# #_*_ coding:utf-8 _*_
# import json
# filename='numbers.json'
# with open(filename) as f_obj:
#     numbers=json.load(f_obj)####读取json文件
# print(numbers)

# import json
# username=input('what is your name?')
# filename='username.json'
# with open(filename,'w')as f_obj:
#     json.dump(username,f_obj)
#     print('we will remember you when you come back,'+username +'!')

# filename='username.json'
# with open(filename) as f_obj:
#     username=json.load(f_obj)
#     print('welcome back,'+username+"!")


# import json
# def greet_user():
#     filename='username.json'
#     try:
#         with open(filename) as f_obj:
#             username=json.load(f_obj)
#     except FileNotFoundError:
#         username=input('what is your name?')
#         with open(filename,'w')as f_obj:
#             json.dump(username,f_obj)
#             print('we will remember you when you come back, '+ username +'!')
#     else:
#         print('welcome back,'+username+'!')
# greet_user()

import json
def get_stored_username():######判断文件是否存在
    filename='username.json'
    try:
        with open(filename)as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():####判断用户名是否存在
    username=input('what is your name?')
    filename='username.json'
    with open(filename,'w')as f_obj:
        json.dump(username,f_obj)

    return username

def greet_user():
    username=get_stored_username()
    shifou=input('zhegemingzishifouzhenque')
    if shifou == 'no':
        username=get_new_username()
    else:
        if username:
            print('welcome back, '+username+' !')
        else:
            # username=input('what is your name?')
            # filename='username.json'
            # with open(filename,'w') as f_obj:
            #     json.dump(username,f_obj)
            username=get_new_username()
            print('we will remember you when you comeback, '+ username +'!')
greet_user()



# file='shuzi.json'
# try:
#     with open(file)as f_obj:
#         shuzi=json.load(f_obj)
# except FileNotFoundError:
#     shuzi = input('what is your favorite number?')
#     with open(file, 'w')as f_obj:
#         json.dump(shuzi, f_obj)
# else:
#     print('i know your favorite number! it is ' + shuzi + ' .')

