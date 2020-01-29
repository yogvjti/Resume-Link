print("** Assignment 5 **")
print("Ex1")
def star(n):
	return(" * "*n)
val = 5
print(star(val))
print("")

print("Ex2")
def print_up_rec(n):
    if n==5:
        print(n,end=" ")
    else:
        print(n,end=" ")
        print_up_rec(n+1)
print_up_rec(1)
print("")

print("Ex3")
def print_up_rec(n):
    if n==1:
        print(n,end=" ")
    else:
        print(n,end=" ")
        print_up_rec(n-1)
print_up_rec(5)
print("")

print("Ex4")
def digitAdd(num):
    sum = 0
    while(num>0):
        d = num%10
        num = num//10
        sum = sum + d
    return(sum)
a = 5012
print(digitAdd(a))
print("")

print("Ex5")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
a = 5
print(factorial(a))