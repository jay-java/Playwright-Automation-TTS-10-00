#Polymorphism -> same function name but having different behaviour
#types- > 2 types
#1.overloading -> not supported
#2.overriding ->
class Parent:
    def add(self,a,b):
        print("add in parent")
        return a+b

    def call(self):
        print("call function parent")

class Child(Parent):
    def add(self,a,b):
        print("add in child")
        super().add(12,12)
        return a+b

    def call(self):
        super().call()
        print("call function child")

p  =  Child()
res=  p.add(1,2)
print(res)
p.call()