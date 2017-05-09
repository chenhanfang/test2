class worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self,percent):
        self.pay *=(1.0 + percent)

bob = worker('bob smith',5000)
print(bob.lastname())
bob.giveraise(.10)
print(bob.pay)
