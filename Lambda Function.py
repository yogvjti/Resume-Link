print("** Assignment 4 **")
print("Ex1")
def Lambda(n):
        return n**2

a = int(input("Enter No: "))
print("Power:",Lambda(a))
print("")

print("Ex2")
def Lambda(a,b):
    return a*b

a = int(input("Enter first no: "))
b = int(input("Enter second no: "))
print("Multiplication:",Lambda(a,b))
print(" ")

print("Ex3")

Ar = [4,34,36,76,68,24,89,23,86,90,45,70]
print("Input List:",Ar)

arr = list(filter(lambda no:(no>=70 and no<=90),Ar))
#arr= list(filter(lambda no:(no>=70 and no<=90),Ar))
print("List after filter: ",arr)

brr = list(map(lambda a:(a+10),arr))
print("List after map: ",brr)

import functools
crr = functools.reduce(lambda a,b:(a*b),brr)
print("Output of reduce:",crr)
print("---------------")
print(" ")

print("Ex4")
A = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
print("Input List:",A)

Br = list(filter(lambda no:(no%2==0),A))
#arr= list(filter(lambda no:(no>=70 and no<=90),Ar))
print("List after filter: ",Br)

Cr = list(map(lambda a:(a**2),Br))
print("List after map: ",Cr)

import functools
Dr = functools.reduce(lambda a,b:(a+b),Cr)
print("Output of reduce:",Dr)
print("---------------")
print(" ")

print("Ex5")
def prime(num):
    for i in range(2,num):
        return(num % i != 0)

Arr = [2,70,11,10,17,23,31,77]
print("Arr = ",Arr)

Brr = list(filter(prime,Arr))
print("Data after filter: ",Brr)

Cr = list(map(lambda a:(a*2),Brr))
print("List after map: ",Cr)

import functools
#Dr = functools.reduce(lambda a,b:(a<b),Cr)
Dr = functools.reduce(lambda a,b:max(a,b),Cr)
print("Output of reduce:",Dr)