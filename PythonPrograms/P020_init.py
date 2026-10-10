# what is init block ?
# init block is special function which invokes automatically when object is created
class Student:
    id = 0
    name = ""
    per = 0

    def __init__(self,id,name,per):
        print("id = ",id)
        print("name = ",name)
        print("per = ",per)

s1 = Student(1,"python",76.67)
s2 = Student(2,"java",87.67)

