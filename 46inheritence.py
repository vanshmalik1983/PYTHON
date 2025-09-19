class employee:
    def __init__(self,name,id):
        self.name= name
        self.id= id

    def showDetails(self):
        print(f"The name of employee : {self.id} is {self.name}")

class programmer(employee):
    def showLanguage(self):
        print("the default language is python")

e1 = employee("rohan das ", 400)
e1.showDetails()
e2 = programmer("vansh ", 500)
e2.showDetails()
e2.showLanguage()
        


class job:
    def __init__(self,name,salary,time):
        self.name = name
        self.salary = salary
        self.time = time

    def showdetails(self):
        print(f"{self.name} gets the {self.salary} from years of {self.time}")


class work(job):
    def showdata(self):
        print(f" {self.name} will get {self.salary} in period of {self.time}")
    
e1 = job("Vansh" , 100000 , 2)
e1.showdetails()
e2 = work("ansh" , 100000 , 1)
e2.showdetails()
e2.showdata()