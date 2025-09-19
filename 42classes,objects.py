class person:
    name = "Vansh"
    occupation = "software eng"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c =person()
a.name = "ansh"
a.occupation = "ca"

b.name = "nikita"
b.occupation = "rn"
# print(a.name , a.occupation)
a.info()  # self ka mtlb jispe mrthod call hora h
b.info()
c.info()