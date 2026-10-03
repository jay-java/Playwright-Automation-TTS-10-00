set = {1,2,3,456.456,True,"python",45756}
print(set)

for x in set:
    print(x)

set.add(23.34)
print(set)

set1 = set.copy()
print(set1)

s1 = {1,2,3}
s2 = {3,4,5,6}

# s1.update(s2)
# print(s1)

s3 = s1.difference(s2)
print(s3)

s4 = s1.union(s2)
print(s4)

s5 = s1.intersection(s2)
print(s5)

