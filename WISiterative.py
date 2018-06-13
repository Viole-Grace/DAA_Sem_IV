#UPDATE : User Input
#Program : Weighted Interval Scheduling - using Iterative Method.
#Time Complexity - O(nlogn), [ O(nlogn) to sort jobs + O(n) to put intervals back together. ]

#Uses a list of list representation ; Inner list elements : Start | End | Weight.
#Given Code's Complexity : O(n*n)
******************************************************************************************************************************
#intervals=[[0, 3, 2],[1,4,4],[3,5,4],[2,6,7],[5,7,2]]
intervals = []
n=int(raw_input("Enter no. of jobs : "))
for i in range(n):
	joblist=[]
	print "\nEnter values for Job ",i+1," : "
	start=int(raw_input("Enter start  : "))
	time=int(raw_input("Enter time : "))
	weight=int(raw_input("Enter weight : "))
	joblist.append(start);joblist.append(time);joblist.append(weight)
	intervals.append(joblist)
intervals.sort(key=lambda x:x[1])
p=[0]*(len(intervals)+1)
m=[-1]*(len(intervals)+1)
m[0]=0
def predecessor():
	for i in range(len(intervals)-1,-1,-1):
		start_time=intervals[i][0]
		for j in range(i-1,-1,-1):
			end_time=intervals[j][1]
			if end_time<=start_time:
				p[i+1]=j+1
				break
def OPT():
	for i in range(1,len(intervals)+1):
		v=intervals[i-1][2]
		m[i]=max(v+m[p[i]],m[i-1])
def solution():
	final_set=[]
	profit=0
	j=len(intervals)
	while j!=0:
		if intervals[j-1][2]+m[p[j]]>m[j-1]:
			final_set.append(j)
			profit+=intervals[j-1][2]
			j=p[j]
		else:
			j=j-1
	return profit,final_set
predecessor()
OPT()
profit,final_set=solution()
print "\nTotal value : ",profit
print "Intervals selected : ",final_set
