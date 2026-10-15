#wrapping data into single unit
class User:
    #__ to declare variable private
    __id =0
    __name = ""
    __contact =0

    def __init__(self,id,name,contact):
        self.__id = id
        self.__name = name
        self.__contact = contact
        print("id= ",id)
        print("name= ",name)
        print("contact= ",contact)

    def printUser(self):
        print("id= ",self.__id)
        print("name= ",self.__name)
        print("contact= ",self.__contact)

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id
u1  = User(1,"python",98765321)
u1.printUser()

u1.setId(13)