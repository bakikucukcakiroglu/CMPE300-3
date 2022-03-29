
import random
import sys
import math
import time


isAvailable=[]
Column=[]


def updateAvailable(row, column, n):

	incrementer=1

	for i in range(row+1,n):

		if( column in isAvailable[i]): 

			isAvailable[i].remove(column)

		if( column+incrementer in isAvailable[i]):

			isAvailable[i].remove(column+incrementer)

		if(column-incrementer in isAvailable[i]):

			isAvailable[i].remove(column-incrementer)

		incrementer=incrementer+1


def QueensLasVegas (n,file1):

	isAvailable.clear()
	Column.clear()

	for i in range(0,n+1):
		isAvailable.append([])
		
		if i!=n:

			isAvailable[i].extend(range(0,n))
	
	R=0
	
	while (len(isAvailable[R])!=0 and R <= n-1):

		index=random.randint(0,len(isAvailable[R])-1)

		Column.append( isAvailable[R][index] )

		updateAvailable(R,isAvailable[R][index], n)	
		
		R = R+1

		file1.write(f"Step {R}: Columns: {Column}\n")	

		file1.write(f"Step {R}: Available: {isAvailable[R]}\n")

	if (len(Column)==n):

		file1.write(f"Successful\n\n")
		return 1
	else:
		file1.write(f"Unsuccessful\n\n")
		return 0


def partA():

	list_n=[6,8,10]

	for n in list_n:

		a= "result_"+str(n)+".txt"

		with open(a, "w") as file1:


			print(f"LasVegas Algorithm With n = {n}")

			success_count=0
			for times in range(0,10000):

				success_count=success_count+QueensLasVegas(n,file1)

			print(f"Number of successful placements is {success_count}")
			print(f"Number of trials is 10000")
			print(f"Probabilty that it will come to a solution is {float(success_count)/float(10000)}\n")


def isValid():

	rowId= len(Column)-1

	for i in range(0,rowId):

		diff= abs(Column[i]-Column[rowId])

		if(diff==0 or diff==rowId-i):

			return False

	return True


def partB():

	list_n=[6,8,10]


	for n in list_n:

		print(f"-----------------{n}-----------------")

		for k in range(0, n):

			success_count=0;

			times=0
			while(times<10000):

				if(QueensLasVegas2 (n,k)):

					times=times+1

					suc=0
					
					if(QueensLasVegasRec(n,k)):

						suc=1

					success_count=success_count+suc

			print(f"k is {k}")
			print(f"Number of successful placements is {success_count}")
			print(f"Number of trials {10000}")
			print(f"Probabilty that it will come to a solution iss {float(success_count)/float(10000)}\n")


def QueensLasVegasRec(n, row):

	if(n==row ):

		return True

	else:


		for i in  range(0,n):

			Column.append(i)

			if(isValid()):

				if(QueensLasVegasRec(n, row+1)):
					return True

			del Column[-1]



def QueensLasVegas2 (n,k):

	isAvailable.clear()
	Column.clear()

	for i in range(0,n+1):
		isAvailable.append([])
		
		if i!=n:

			isAvailable[i].extend(range(0,n))
	
	R=0
	
	while (len(isAvailable[R])!=0 and R <= k-1):

		index=random.randint(0,len(isAvailable[R])-1)


		Column.append( isAvailable[R][index])

		updateAvailable(R,isAvailable[R][index], n)	
		
		R = R+1

	if (len(Column)==k):

		return 1
	else:
		return 0


if(sys.argv[1]=="part1"):

	partA()

elif(sys.argv[1]=="part2"):

	partB()

