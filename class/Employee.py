class Employee():
    def __init__(self,first,last,xinzi):
        self.firstname=first
        self.lastname=last
        self.xinzi=xinzi
    def give_raise(self,default=5000):
        self.default=default
        self.xinzi=self.xinzi+self.default
        return self.xinzi

# eml=Employee('ce','ce',8000)
# eml.give_raise()
# print(eml.xinzi)