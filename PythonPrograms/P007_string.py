#    012345678901234567  +
s = "Tops techonologies"
#    876543210987654321  -
print(s)
print(type(s))
print(len(s))
print(s.isspace())
print(s.isnumeric())
print(s.isalpha())
print(s.isalnum())
print(s.find(""))
print(s.index("o",5))
print(s.count("o"))
print(s.startswith("Top"))
print(s.endswith("p"))
print(s.center(40,"-"))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
s1 = "      TO PS          "
print(s1.strip())
print(s1.lstrip())


#String slicing
#    012345678901234567  +
s = "Python Programming"
#    876543210987654321  -
print("==========")
print(s[-1])
print(s[2:10])
print(s[2:12:2])
print(s[4:])
print(s[1::2])
print(s[:-2])
print(s[-16:-4:2])
