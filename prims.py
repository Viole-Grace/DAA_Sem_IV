#Prim's Algorithm - Provides an MST for a Graph
#Greedy Algorithm
#Time Complexity - O(ElogV)
#Uses - Cluster analysis : k clustering problem can be viewed as finding an MST and deleting the k-1 most expensive edges.
#Works best when no. of edges < = no. of nodes in the graph

############################################################################################################################################
import time
graph=dict()
n=int(raw_input("Enter no. of nodes in the graph : "))
for i in range(n):
	node=int(raw_input("\nEnter node : "))
	k=int(raw_input("Enter no. of nodes it is connected to : "))
	nodelist=dict()
	for j in range(k):
		nd=int(raw_input("Enter connected node : "))
		ed=int(raw_input("Enter edge weight : "))
		nodelist.update({nd:ed})
	graph.update({node:nodelist})
def Prims():
	U,V=set([1]),set(graph.keys())
	result = []
	while len(U) != len(V) :
		minw = -1
		mine = []
		for u in U:
			for v in graph[u]:
				if v in V-U:
					if minw == -1 or minw > graph[u][v]:
						minw = graph[u][v]
						mine = [u,v]
		mine.append(minw)
		result.append(mine)
		U.add(mine[1])
	print "\nSpanning Tree Format : \n\nNode --> Node | Edge weight taken"
	for sublist in result: #prints list of list on a new line
		for item in sublist:
			print item,
		print " "
start = time.clock()
Prims()
end = time.clock()
print "Running time - ",end-start," seconds"
