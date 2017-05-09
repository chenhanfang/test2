class Programer(object):
    hobby='play computer'

    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight


    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_inturoduction(self):
        print('My name is %s \nI am %s years old\n'%(self.name,self._age))

    # def get_weight(self):
    #     return self.__weight

class BackendProgram(Programer):
    def __init__(self,name,age,weight,language):
        super(BackendProgram,self).__init__(name,age,weight)
        self.language=language

    def self_inturoduction(self):
        print('My name is %s \nI am %s years old\nI study %s\n'%(self.name,self._age,self.language))

def introduce(programe):
    if isinstance(programe,Programer):
        programe.self_inturoduction()


if __name__=="__main__":
    programe=Programer('Alber',25,100)
    backend_programe=BackendProgram('Tim',24,34,'python')
    print(dir(programe))
    # print(programe.__dict__)
    # print(programe.get_weight())
    # print(programe._Programer__weight)
    # print(Programer.get_hobby())
    # print(programe.get_weight)
    # programe.self_inturoduction()
    # print(type(programe))
    # print(isinstance(programe,Programer))
    # print(issubclass(BackendProgram,Programer))
    introduce(programe)
    introduce(backend_programe)
