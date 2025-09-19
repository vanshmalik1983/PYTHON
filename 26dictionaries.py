dic ={
    "vansh":"human" , 
    "spoon":"object"
}
print(dic["vansh"])
print(dic["spoon"])

dic1 ={
    343:"vansh" , 
    454:"ansh" , 
    345:"kanak"
}
print(dic1[343])

info = {'name':'vansh' , 'age':19 , 'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))
print(info.values())

for key in info.keys():
    print(info[key])

print(info.items())
for key , value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
