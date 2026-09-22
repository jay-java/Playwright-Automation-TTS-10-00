# for /for in
from xml.dom.pulldom import PROCESSING_INSTRUCTION

for i in range(1, 11):
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

