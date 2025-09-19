class emp:
    comp = "apple"
    def show(self):
        print(f" the name is {self.name} and company is {self.comp}")

    @classmethod
    def changecomp(cls,newcomp):
        cls.comp = newcomp

e1 = emp()
e1.name = "vansh"
e1.show()
e1.changecomp("Tesla")
e1.show()
print(emp.comp)