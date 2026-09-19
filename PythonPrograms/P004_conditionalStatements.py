#if else
from subprocess import check_output

a = 10
b = 10
if a >b:
    print('a is greater than b')
else:
    print('a is not greater than b')

#nested if
age = int(input('Enter your age: '))

if age > 18:
    if age <55:
        print('you are eligible')
    else:
        print('age is greater than 18 but not less than 55')
else:
    print('age is less than 18')


#if elif else
per = float(input('Enter your percentage: '))
if per < 35:
    print('failed')
elif per >= 35 and per <=60:
    print('Pass class')
elif per >= 61 and per <=70:
    print('C grade')
elif per >= 71 and per <=80:
    print('B grade')
elif per >= 81 and per <=90:
    print('A grade')
elif per >= 91 and per <=100:
    print('A+ grade')
else:
    print('invalid input')


#match
print('1.English 2.Hindi 3.Gujarati')
choice = int(input('Enter your choice: '))
match choice:
    case 1:
        print('English')
    case 2:
        print('Hindi')
    case 3:
        print('Gujarati')
    case _:
        print('Invalid choice')
