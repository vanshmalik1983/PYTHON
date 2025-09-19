#public private protected 
class employee:
    def __init__(self):
        self.__name = "Vansh"
        

a = employee()
# print(a.__name) #cannot be accessed directly
print(a._employee__name) # can be accessed indirectly
print(a.__dir__())


class students:
    def __init__(self):
        self._name = "vansh"

    def _funname(self):  # protected method

        return "vanshmalik"

class subjects(students):   #inherited class
    pass

obj = students()
obj1 = subjects()
print(dir(obj))

#calling by object of student class
print(obj._name)
print(obj._funname)


#calling by object of student class
print(obj1._name)
print(obj1._funname)

