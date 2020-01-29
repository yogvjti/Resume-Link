import threading
def Square(num):
    n = num ** 2
    print("Square:",n)
	#print("Square:{}".format(num**2))

def Cube(num):
	print("Cube:{}".format(num**3))

if __name__ == "__main__":
	 num = int(input("Input No:"))

	 thread1 = threading.Thread(target=Square,args=(num,))
	 thread2 = threading.Thread(target=Cube,args=(num,))

	 thread1.start()
	 thread2.start()

	 thread1.join()
	 thread2.join()

	 print("Done!")