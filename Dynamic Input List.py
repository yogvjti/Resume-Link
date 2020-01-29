print("** Assignment 3 ***")

List = []
Ar = int(input("Enter no of elements: "))

for i in range(Ar):
    i = int(input("Enter Elements: "))
    List.append(i)

print("List: ",List)

print("Ex1")
print("Sum of elements in list:",sum(List))
print("")

print("Ex2")
print("Maximum no from list: ",max(List))
print("")

print("Ex3")
print("Minimum no from list: ",min(List))
print("")

print("Ex4")
from collections import Counter
x = List[1]
d = Counter(List)
print('{} has occurred {} times'.format(x, d[x]))