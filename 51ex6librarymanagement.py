class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showdInfo(self):
        print(f"The library has {self.nobooks} books . the books are ")
        for book in self.books:
            print(book)

l1 = library()
l1.addbook("vansh malik")
l1.addbook("vansh malik1")
l1.addbook("vansh malik2")
l1.addbook("vansh malik3")
l1.addbook("vansh malik4")
l1.addbook("vansh malik5")
l1.showdInfo()