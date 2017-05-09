class Programer(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

# '''获取属性设置'''
    def __getattribute__(self,name):
        return super(Programer,self).__getattribute__(name)
        # return getattr(self,name)#错误的写法，引起无限递归
        # return self.__dict__[name]#错误的写法

# '''设置属性设置'''
    def __setattr__(self,name,value):
        # setattr(self,name,value)#错误的写法
        self.__dict__[name]=value

if __name__=='__main__':
    p=Programer('Alter',24)
    print(p.name )