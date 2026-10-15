#access property of one class to another class
#to make our code reusable
#types
# 1.single
# 2.multileve
# 3.multiple
# 4.hierarchical
# 5.hybrid

#single
class A:
    def classA(self):
        print("class A function")

class B(A):
    def classB(self):
        print("class B function")

#multilevel
class C(B):
    def classC(self):
        print("class C function")

b = B()
b.classA()
b.classB()

c  =C()
c.classA()
c.classB()
c.classC()


#multiple
class A1:
    def classA1(self):
        print("class A1 function")
class B1:
    def classB1(self):
        print("class B1 function")
class C1(A1,B1):
    def classC1(self):
        print("class C1 function")

c = C1()
c.classA1()
c.classB1()
c.classC1()


#Hierarchical
class AA:
    def classAA(self):
        print("class A function")
class BB(AA):
    def classBB(self):
        print("class B function")
class CC(AA):
    def classCC(self):
        print("class C function")

b =BB()
b.classAA()
b.classBB()
c = CC()
c.classAA()
c.classCC()

#hybrid