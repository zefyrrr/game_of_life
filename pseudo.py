import random




# RULES
#    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#    Any live cell with two or three live neighbours lives on to the next generation.
#    Any live cell with more than three live neighbours dies, as if by overcrowding.
#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# FEATURES

# User input to create seed cells
# Have a list of standard initial cell positions
# Aility to change the rules either initially by design or later by algorithm

# Initialize Variables
# use appropriate graphics library

# To Do
# Representation of cells
# c1, x_pos, y_pos
# c2, x_pos, y_pos
# cells come and go, time accumulates
# cn, x_pos, y_pos

# Check adjacency

#for each element
# check if any of the other elements are close by
#
#if element x/y = x+1/y+1 then neighbour++
#if neighbor < 
#
#when deleting a cell, mark its position
#
#x,y,n
#
#make it a class:
#	a pixel is a class, update the objects and print the list
#
#update it on a timer

x = [ [ 2, 3, 4 ] , [ 3, 6, 0 ] ]
x.append("hello world")
#print x
#del x[1]
#print x


for i in range(10):
	x.append([random.randint(0, 5),random.randint(0, 5),random.randint(0, 5)])

mylist = list(set(x))

for i in range(len(mylist)):
	print myslit[i]

# Iterate through simulation
# Check environment around cell
# compare Cx, x_pos, y_pos with adjacent 8 cell positions. count and add, if <2 then die, #if more than 3 then also die. 
# there is something missing here about the potential of a future adjacent cell


# Spawn child or die at appropriate position

