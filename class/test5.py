
class Programer(object):

    def __init__(self,name,age):
        self.name=name
        if isinstance(age,int):
            self.age=age
        else:
            raise Exception('age must be int')

    # def __eq__(self,other):
    #     if isinstance(other,Programer):
    #         if self.age==other.age:
    #             return True
    #         else:
    #             return False
    #     else:
    #         raise Exception('the type of object must be programer')

    def __add__(self, other):
        if isinstance(other,Programer):
            return self.age+other.age
        else:
            raise Exception('the type of object must be programer')

    def __eq__(self, other):
        if isinstance(other,Programer):
            if self.name==other.name:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be programer')

    def __gt__(self,other):
        if isinstance(other,Programer):
            if self.age > other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be programer')

if __name__=='__main__':
    p1= Programer('Alter',36)
    p2= Programer('Tim',27)
    print(p1>p2)
    print(p1==p2)
    print(p1+p2)
