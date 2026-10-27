# abnormal situation occurs at runtime
# try except finally
# to maintain flow of code
try:
    a = int(input("enter a = "))
    b = int(input("enter b = "))

    c = a / b
    print(c)

except ZeroDivisionError as e:
    print("cannot divide by zero")

except ValueError as e:
    print("denominator should be integer")

except Exception as e:
    print(e)

finally:
    print("finally block  will executes everytime")
