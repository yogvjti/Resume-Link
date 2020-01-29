class Demo:
    Value = 50
    def __init__(self,no1,no2):
        self.i= no1
        self.j= no2

    def fun(self):
        print(self.i,self.j)

    def gun(self):
        print(self.i,self.j)


def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    print("Fun:")
    obj1.fun()
    obj2.fun()

    print("Gun:")
    obj1.gun()
    obj2.gun()

    print("Done!")
if __name__=="__main__":
    main()


print("="*30)

class Circle:
    PI = 3.14;

    def __init__(self,radius):
        self.R = radius

    def Accept(self):
        print(self.R)
        #print("Radius is:"self.R)

    def area(self):
        print(self.R**2*3.14)

    def circum(self):
        print(2*self.R*3.14)

    @classmethod
    def DisplayPI(cls):
        print(cls.PI)

#obj = Circle(3)

R = int(input("Enter radius of circle: "))
obj = Circle(R)

print("Radius is:")
obj.Accept()

print("Area is:")
obj.area()

print("Circumference is: ")
obj.circum()

print("Value of PI: ")
obj.DisplayPI()


print("-----------------------------")

class Circle:
    PI = 3.14;

    def __init__(self,radius):
        self.R = radius

    def Accept(self):
        print("Radius is: ",self.R)
        print(self.R)

    def area(self):
        print("Area is: ",self.R**2*3.14)

    def circum(self):
        print("Circumference is: ",2*self.R*3.14)

    @classmethod
    def DisplayPI(cls):
        print("Value of PI:",cls.PI)

def main():

    Newcircle = Circle(3)
    print(Newcircle.Accept())
    print(Newcircle.area())
    print(Newcircle.circum())
    print(Newcircle.DisplayPI())

    print("Done!")

if __name__=="__main__":
    main()

print("="*30)

class Arithmetic:
    Value = 0

    def __init__(self,Value1,Value2):
        self.i = Value1
        self.j = Value2

    def Accept(self):
        print("Accepted Numbers:",self.i,self.j)

    def Addition(self):
        print("Addition is:",self.i + self.j)

    def Subtraction(self):
        print("Sub is:",self.i - self.j)

    def Multiplication(self):
        print("Multi is:",self.i * self.j)

    def Division(self):
        print("Div is:", self.i / self.j)

def main():

    obj1 = Arithmetic(200,50);
    obj1.Accept();
    obj1.Addition();
    obj1.Subtraction();
    obj1.Multiplication();
    obj1.Division();

if __name__=="__main__":
    main()