print("** Assignment 2 **")
print("Ex1")
import Assignment2
def main():
    a = int(input("Enter no1: "))
    b = int(input("Enter no2: "))

    add = Assignment2.Add(a,b)
    sub = Assignment2.Sub(a,b)
    mul = Assignment2.Mult(a,b)
    div = Assignment2.Div(a,b)

    print("Addition: ",add)
    print("Subtraction: ",sub)
    print("Multiplication: ",mul)
    print("Division: ",div)

if __name__=="__main__":
    main()
print("---------------------")
print(" ")

print("Ex9")
def digit(num):
    count = 0
    while (num>0):
        num = num//10
        count = count + 1
    return (count)

def main():
    a = int(input("Enter no: "))
    b = digit(a)
    print("No of digits in {} is {}".format(a,b))
if __name__ =="__main__":
    main()
print("---------------------")
print(" ")

print("Ex10")
def digitAdd(num):
    sum = 0
    while(num>0):
        d = num%10
        num = num//10
        sum = sum + d
    return(sum)

def main():
    a = int(input("Enter no.: "))
    b = digitAdd(a)
    print("Sum of digits in",a,"is",b)

if __name__ =="__main__":
    main()
print("---------------------")
print(" ")

print("Ex5")
def check(no):
    if (num>1):
        for i in range(2,num//2):
            if(num % i) ==0:
                print(num,"is not prime")
                break
            else:
                print(num,"is prime number")
    else:
        print(num,"is not prime number")

num = int(input("Enter no: "))
check(num)
print("---------------------")
print(" ")

print("Ex4")
def factor(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i;
    return(sum);
def main():
    a = int(input("Enter no: "))
    b = factor(a)
    print("Sum of factors of",a,"is",b)
if __name__=="__main__":
    main()