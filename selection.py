#Selection Sort - Sorts the smallest element of the array first [ Exact Opposite of Bubble Sort ]
#Time Complexity - O(n*n)
#Uses - Writing / Swapping on Flash Memory [ O(n) number of swaps ], Sorting Small unsorted arrays (size < 20)

#################################################################################################################################

import random
import time
L = []
for i in range(1000):
    L.append(random.randint(0,1001))
start=time.clock()
for i in range(len(L)):
    m=i
    for j in range(i+1,len(L)):
        if L[j] < L[m]:
            m=j
    L[i],L[m]=L[m],L[i]
end=time.clock()
print L
print ("The program ran for:")
print (end-start)
print ("seconds")
