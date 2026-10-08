
def fun1():
    print('fun 1')

    def fun2():
        print('fun 2')

    fun2()

fun1()

# Lambda functions- >anonymous function, they do not have a defined name

name = 'python programming'
# funName = lambda i(argument/parameter) : expression

nameUpper = lambda i: i.upper()
print(nameUpper(name))

checkNumber = lambda a: 'greater than 0' if a > 0 else 'less than 0' if a < 0 else 'zero'
res = checkNumber(12)
print(res)
print(checkNumber(-54))

add = lambda a, b: (a + b, a / b)
addition = add(2, 3)
print(addition)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda i: i % 2 == 0, nums)
print(list(even))
