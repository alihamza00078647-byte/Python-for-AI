class _2Dvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")
    
class _3Dvector(_2Dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a = _2Dvector(1, 2)
a.show()
b = _3Dvector(3, 5, 8)
b.show()