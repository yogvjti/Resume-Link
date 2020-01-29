print("*** ASSIGNMENT 1 ***")
print("   ")
print("Ex1")
def fun():
    print("Hello from fun")
fun()
print("    ")

print("Ex2")
def no():
    n = int(input("Any no:"))
    if (n%2==0):
        print("EVEN")
    else:
        print("Odd")
no()
print("     ")

print("Ex3")
def Add():
    a = int(input("First no:"))
    b = int(input("Second no:"))
    sum =(a+b)
    print("Adddition of no is {}".format(sum))
Add()
print("     ")

print("Ex4")
def name(n):
	if n != 0:
		name(n-1)
		print("Marvellous")
name(5)
print("     ")

print("Ex5")
def num():
    u = 0
    v = 10
    for num in range(v, u,-1):
        print(num,end="  ")
num()
print("     ")
print("     ")

print("Ex6")
def CheckN():
    n = int(input("Enter N:"))
    if (n>0):
        print("Positive")
    elif (n<0):
        print("Negative")
    else:
        print("Zero")
CheckN()
print("     ")

print("Ex7")
def Bool(n):
    return True if n % 5 == 0 else False

print(Bool(10))
print("     ")

print("Ex8")
def star():
    a = int(input("Enter No of stars: "))
    print(" * "*a)
star()
print("     ")

print("Ex9")
def Even():
    a = int(input("Enter Interval: "))
    for Even in range(2,21,a):
        print(Even,end="  ")
Even()
print("     ")
print("     ")

print("Ex10")
def name():
    str = input("Enter name:")
    print(len(str))
name()

def str(name):
    return len(name)
a = input("Enter Name: ")
print("No of alphabets: ",str(a))