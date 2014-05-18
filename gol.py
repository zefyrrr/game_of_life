import random
from javax.swing import *
from java.awt import *
import time


class Grid(JPanel):
	def __init__(self, dimension, seedLoad, pixelScaleFactor):
		super(Grid, self).__init__()
		self.grid = set()
		for i in range(0, int(dimension * dimension * seedLoad)):
			x = random.randint(0, dimension - 1)
			y = random.randint(0, dimension - 1)
			self.grid.add((x,y))

		self.dimension = dimension
		self.pixelScaleFactor = pixelScaleFactor
	

	def getNeighbours(self, x, y):
		neighbours = []
		for i in range(0, 3):
			for j in range(0, 3):
				if i == 1 and j == 1:
					continue
				neigbhourX = x - 1 + i
				neigbhourY = y - 1 + j
				if neigbhourX >= self.dimension or neigbhourY >= self.dimension:
					continue
				neighbours.append((neigbhourX, neigbhourY))
		return neighbours

	def getAliveCount(self, candidates):
		aliveCount = 0
		for (x,y) in candidates:
			if (x,y) in self.grid:
				aliveCount = aliveCount + 1
		return aliveCount


	def tick(self):
		newGrid = set()
		for (x,y) in self.grid:

			neighbours = self.getNeighbours(x, y)
			aliveCount = self.getAliveCount(neighbours)

			# Rules
			# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
			# 2. Any live cell with two or three live neighbours lives on to the next generation.
			# 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
			# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

			if aliveCount == 2 or aliveCount == 3:
				newGrid.add((x,y))

			for (neigbhourX, neigbhourY) in neighbours:
				theirNeighbours = self.getNeighbours(neigbhourX, neigbhourY)
				if self.getAliveCount(theirNeighbours) == 3:
					newGrid.add((neigbhourX, neigbhourY))

		self.grid = newGrid
	
	def paintComponent(self, g):
		self.tick()
		g.setColor(Color(31, 21, 1))
		for (x, y) in self.grid:
			x = x * self.pixelScaleFactor
			y = y * self.pixelScaleFactor
			g.fillRect(x, y,  self.pixelScaleFactor, self.pixelScaleFactor)



def main():
	frame = JFrame("Game of Life")
	
	pixelScaleFactor = 10;
	dimension = 100
	seedLoad = 0.5
	
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	
	bounds = GraphicsEnvironment.getLocalGraphicsEnvironment().getMaximumWindowBounds()
	width = (dimension * pixelScaleFactor) + int(bounds.getX())
	height = (dimension * pixelScaleFactor) + int(bounds.getY())
	frame.setSize(width, height)
	frame.setResizable(False)
	
	grid = Grid(dimension, seedLoad, pixelScaleFactor)
	frame.getContentPane().add(grid)
	frame.show()
	

	for i in range(0,10000):
		time.sleep(0.05)
		grid.repaint()


if __name__ == "__main__":
    main()