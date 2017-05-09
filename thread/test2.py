def hello():
    print('Hello,World.')
print(dir(hello))

def hello(numa,numb=1,numc=[]):
    print(numa,numb,numc)
    return True
# print(hello.__name__)
# print(hello.__doc__)
# print(hello.__module__)
# print(hello.__dict__)
# print(hello.__defaults__)
#
# hello.name='xiaoming'####给方法增加一个属性
# print(hello.__dict__)
# hello.__dict__['name']='xiaoming'
# print(hello.name)

hello.__defaults__[1].append('hello')
hello(100)