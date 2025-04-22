class student:
    def __init__ (self,name,roll,m1,m2):
        self.n1 = name
        self.n2 = roll
        self.n3 = m1
        self.n4 = m2
    def Print(self):
        print(self.n1,self.n2,self.n3,self.n4)
    def Avg(self):
        print((self.n3+self.n4)/2)
ob1 = student("a",12,89,82)
ob2 = student("b",11,90,80)
ob1.Print()
ob1.Avg()
ob2.Avg()
