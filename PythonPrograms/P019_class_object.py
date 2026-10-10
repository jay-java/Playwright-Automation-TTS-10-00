# class-> is structure in which we can have member functions and member variables
# object- > Object instance of class, with state and behavior

class User:
    id = 0
    name =""
    contact =0

    def __init__(self):
        print("this is init")

    def setId(self,id):
        print("id = ",id)

    def setName(self,name):
        print("name = ",name)

    def setContact(self,contact):
        print("contact = ",contact)

#syntax to create object
# objectName = ClassNme()

u1 = User()
u1.setId(12)
u1.setName("python")
u1.setContact(987634231)
print(u1.id)
print(u1.name)
print(u1.contact)

