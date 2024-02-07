class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


class Book:
    def __init__(self, input1, input2):
        self.bookid = input1
        self.bookstatus = input2


class Library:
    def __init__(self, input1, input2):
        self.libraryid = input1
        self.librarycap = input2
        self.librarybook = [input2]


nol = int(input("Enter the number of libraries\n"))
nob = int(input("Enter the number of books in each library\n"))
lbr = []
lbr.extend(range(nol))

for i in range(nol):
    lbr[i] = Library(i, nob)
    print(f"lbr{i}")
for i in range(nol):
    lbr[i].librarybook.extend(range(nob))
    for j in range(nob):
        lbr[i].librarybook[j] = Book(1000 * i + j, True)


def borrowbook(idn):
    bookfound = False
    for i1 in range(nol):
        if not bookfound:
            for j1 in range(nob):
                if idn == lbr[i1].librarybook[j1].bookid and lbr[i1].librarybook[j1].bookstatus:
                    print(f"The Book {idn} Is Borrwed Successfully")
                    lbr[i1].librarybook[j1].bookstatus = False
                    bookfound = True
                    break
                elif idn == lbr[i1].librarybook[j1].bookid:
                    print(f"The Book {idn} Is Already Borrwed")
                    break
    if not bookfound:
        print(f"Book {idn} Not Found")


while True:
    print("Enter the Id of a book you want to borrow:")
    id1 = int(input())
    borrowbook(id1)
