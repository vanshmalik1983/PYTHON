class emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], string.split("-")[1])
    
e1 = emp("vansh" , 200)
print(e1.name)
print(e1.salary)

string = "john-200"
# e2 = emp(string.split("-")[0] ,string.split("-")[1] )
e2 =emp.fromstr(string)
print(e2.name)
print(e2.salary)

        