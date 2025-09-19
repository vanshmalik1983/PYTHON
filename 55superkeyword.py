class parentclass:
    def parent_method(self):
        print(f"this is the parent method1")

class childclass(parentclass):
    def parent_method(self):
        print("vansh")
        super().parent_method()
    def child_method(self):
        print("this is a child method2 .")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()




        

