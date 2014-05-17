import random
duplicate = 0
myList = []
for i in range(1000):
    myList.append([random.randint(0, 100),random.randint(0, 100)], 'unknown')
    
orig_len = len(myList)

#    Returns 1 if adjacent
#    Returns -1 if duplicate
#    Returns 0 if neither
def compare_adjacency(x,y):   
    if x == y: # Duplicate
        return -1 
    if (y[0] >= x[0] - 1 and y[0] <= x[0] + 1) and (y[1] >= x[1] - 1 and y[1] <= x[1] + 1) :
        return 1
    return 0
    
length = len(myList)
    
h=0

while h < len(myList):
    match = 0
    i = 0
#    for i in range((length -1) , 0, -1):
    while i < len(myList): # make sure our index stays in bounds

        if h == i: #skip
            break  # iterate to the next element
        ret_val = compare_adjacency(myList[h],myList[i]) # retrieve list item comparison
        
        if ret_val == -1: # Duplicate
#            print "Duplicate", myList[h],myList[i], h, i
            duplicate = duplicate + 1
            del myList[i]
            break

        if ret_val == 1:
            match = match + 1
#            print "Match", myList[h], myList[i], match
#        if ret_val == 0:
#            print "No Match"
        i = i+1
    #I will live
    if match > 1  and match < 4:
        print "Cell #", h, "has", match, "matches, is happy and will survive"
        
    #I will divide_and_multiply
#        are there three cells around a dead cell
        
    #I will die
    if match < 2 :
        print "Cell #", h, "has", match, "matches, is lonely and will die"
    
    if match > 3:
        print "Cell #", h, "has", match, "matches, is overcrowded and will die"
    h = h + 1


print "original length =", orig_len, "final length =", len(myList)
print "Number of duplicates =", duplicate
#I will live




 
#for a in range(len(myList)):
#    print myList[a][0],
#    print myList[a][1]




#print compare_adjacency([1,2],[3,2])
