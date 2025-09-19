x = [1,2,3]
# x = (1,2,3)
print(dir(x))  #functions in it  
print(x.__gt__)

# DICT  
class person:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age 
        self.version = 1
        self.salary = salary
p = person("vansh",19,1000000)
print(p.__dict__) # givs as a dictionary

print(help(person))
# print(help(str))