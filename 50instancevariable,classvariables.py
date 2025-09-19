class employee:
    comname = "apple"
    noofemployee = 0
    def __init__(self,name):
        self.name = name 
        self.raise_amount = 0.02
        employee.noofemployee +=1
    def showDetails(self):
            print(f"the name of employee is {self.name} and the raise amount in {self.noofemployee} sized {self.comname}  is {self.raise_amount}")

# emp1.showDetails()
emp1 = employee("vansh")
emp1.raise_amount = 0.056
emp1.comname = "Apple India"
employee.showDetails(emp1)
employee.comname = "Google"
print(employee.comname)
emp2 = employee("kanak")
employee.showDetails(emp2)