#strngs are immutable(non changeable)
a = "vansh!!!!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Vansh","Harry"))
print(a.split(" "))
print(a.capitalize())
print(a.center(100))
print(len(a.center(100)))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!?"))
print(str1.endswith("to",4,10))

str2 = "He's name is vansh. He is an honest man."
print(str2.find("is"))
print(str2.index("is"))

str3 = "Welcome Health "
print(str3.isalpha())
print(str3.islower())
print(str3.istitle())
print(str3.swapcase())
