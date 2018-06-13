#Counting Inversions - Rudimentary Method. Uses Brute-Forcing
#Time Complexity - O(nlogn) using Modified Merge Sort.
#Given Code's Time Complexity - O(n*n)
#Uses - Inversion Count for an array indicates  how far (or close) the array is from being sorted.
#No. of inversions = MAX if array is sorted in reverse order, i.e, descending order

################################################################################################################################
import time
L= []
n=int(raw_input("Enter range of array : "))
for i in range(n):
	print "Enter element ",i+1,"of the array : "
	L.append(int(raw_input()))
print "Array :",L
def inversion(list1,n):
	count=0;
	for i in range(n):
		for j in range(i+1,n):
			if(list1[i]>list1[j]):
				count=count+1
	print "No. of inversions for the given array : ",count
start=time.clock()
inversion(L,len(L))
end=time.clock()
print "Time taken to count no. of inversions : "(end-start)," seconds"
