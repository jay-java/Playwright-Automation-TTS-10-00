list = [1,2,3,4,5,12,"name",True,435.6456,45676,1]
print(list)
print(len(list))
print(list[0])
list.append(12)
print(list)
print(list.count(2))
list.insert(1,"python")
print(list)

print(list.index(12,7))
print(list)

list.remove(12)
print(list)

list.pop()
print(list)

new_list = list.copy()
print(new_list)

list1 = [1,2,3]
print(len(new_list))
# new_list.extend(list1)
print(new_list)

new_list.append(list1)
print(new_list)
print(len(new_list))
print(new_list[10][1])


# list.reverse()

for i in list:
    print(i)
