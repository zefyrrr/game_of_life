import random

myList = []
for i in range(25):
	myList.append([random.randint(0, 5),random.randint(0, 5)])

#print myList

def compare_adjacency(x,y):
	print range(len(x))
	
	if x == y:
		return -1 
	if (y[0] >= x[0] - 1 and y[0] <= x[0] + 1) and (y[1] >= x[1] - 1 and y[1] <= x[1] + 1) :
		return 1
	return 0
	

	

# Iterate through the loop until a match is reached
#loop = True
#while loop:
#	myList[0] = ([random.randint(0, 25),random.randint(0, 25)])
#		if myList[0] == myList[1]:
#			print "True!",
#			loop = False
#		else:
#			print "False!",
#		c = c + 1
#		print c

# Go through the loop a set number of times
length = len(myList)
#match = 0
for h in range(length):
    match = 0
    for i in range(length):
		if h == i:
			print "Skip"
			break
		
		ret_val = compare_adjacency(myList[h],myList[i])
		
		if ret_val == -1:
			print "Duplicate"
		
		if ret_val == 1:
			match = match + 1
			print "Match", myList[h], myList[i], match
		if ret_val == 0:
			print "No Match"


#I will live
#I will die
#I will divide_and_multiply


 
#for a in range(len(myList)):
#	print myList[a][0],
#	print myList[a][1]




#print compare_adjacency([1,2],[3,2])
