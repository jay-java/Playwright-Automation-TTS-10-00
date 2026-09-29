# for /for in

for i in range(5, 11):
    print(i)

for a in range(10):
    print(a)

# while
# ( < , +) ( > ,-)
j = 1
while j <= 5:
    print(j)
    j = j + 1

k = 5
while k >= 1:
    print(k)
    k = k - 1


for i in range(1,6): #row
    for j in range(1,6): #column
        print("*",end='')
    print()

for i in range(1,6): #row
    for j in range(1,i+1): #column
        print("*",end='')
    print()


for i in range(10,0,-1):
    print(i)


for i in range(1,6): #row
    for s in range(4,i-1,-1):
        print(" ",end='')
    for j in range(1,i+1): #column
        print("*",end='')
    print()

for i in range(1,6): #row
    for s in range(4,i-1,-1):
        print(" ",end='')
    for j in range(1,i+1): #column
        print("* ",end='')
    print()

for i in range(1,6):
    for s in range(2,i+1):
        print(" ",end='')
    for j in range(5,i-1,-1):
        print("* ",end='')
    print()

num =1
for i1 in range(1,6):
    for j1 in range(1,i1+1):
        print(num,end=' ')
        num = num + 1
    print()

for i1 in range(1,6):
    for j1 in range(1,i1+1):
        # print('i1 = ',i1,'j1 = ',j1,end='->')
        if (i1+j1) % 2 == 0:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()


