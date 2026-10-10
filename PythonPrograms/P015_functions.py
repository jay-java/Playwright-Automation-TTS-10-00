# function is block of code to perform specific task
# Types of function :
# 1.Pre-define
# 2.user define

# there are 4 ways to define function
# 1.without return type without parameter
def funName():
    print('this is without return type without parameter function')


# 2.without return type with parameter
def funWithParameter(n):
    # print('this is without return type with parameter function : ',n)
    if (n % 2 == 0):
        print(n, 'is even')
    else:
        print(n, 'is odd')


# default argument in function
def myfunction(a, b=12):
    print('a = ', a, ' b = ', b)


# keyword argument
# Positional argument
def name(fname, lname):
    print(fname, lname)


# Arbitary argument
# * -> asterisk
# *args -> collects all arguments as a tuple
# **kwargs -> collects all argument as dictionary
def arbitaryFun(*args):
    for i in args:
        print(i)


def arbitaryKwargsFun(**kwargs):
    for key, value in kwargs.items():
        print(key, ' : ', value)


# fname,lname,con,address,email,password,gender
def createAccount(*args):
    for i in args:
        print(i)


# 3.with return type without parameter
def funName1():
    print('with return type without parameter')
    return 321.145


# 4.with return type with parameter
def squareOfNum(num):
    print('number coming from parameter', num)
    return num * num


#execution start(all functions start calling from here)
funName()
funWithParameter(12)
myfunction(34,45)
name('Python', 'Programming')
name(lname='Python', fname='Programming')
name(1, 'java')
arbitaryFun('hi', 'Python', 123)
arbitaryKwargsFun(fname='python', lanme='java', lang='php')
createAccount("firstname","lastname",987654,"ahmedabad","email@gmail.com","password")
val = funName1()
print(val)

num = int(input('enter number'))
sq = squareOfNum(num)
print('square of', num, 'is', sq)











