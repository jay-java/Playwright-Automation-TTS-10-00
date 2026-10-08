d1 = {
    1:"c",
    2:"c++",
    3:"python",
    "java":False,
    5:346.46,
    6:"c"
}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

d2 = {
    10:"python",
    11:"playwright"
}

d1.update(d2)
print(d1)

print(d1.get(2))

for i in d1:
    print(i, " : ",d1[i])

print("=============")

for j in d1.items():
    print(j)





