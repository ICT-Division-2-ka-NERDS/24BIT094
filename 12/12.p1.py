class Area:
    def __init__ (self,length,breadth):
        self.n1 = length * breadth
        self.n2 = 2*(length+breadth)
    def set_n(self, length, breadth):
        self.n1 = length * breadth
        self.n2 = 2 *(length+breadth)
    def Print(self):
        print(f"area = {self.n1} , perimeter = {self.n2}")
    def get_n(self):
        return self.n1, self.n2
ob1 = Area() #object instantiation
ob1.set_n(10,20)
ob1.Print()

ob2 = Area()
ob2.set_n(10.1,20.1)
print(ob1.get_n())
a,b = ob2.get_n()
print(a,b)

ob3 = Area(10,20)
