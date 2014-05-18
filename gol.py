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



    def paintComponent(self, g):
	    g.setColor(Color(31, 21, 1))
	    for (x, y) in self.grid:
			x = x * self.pixelScaleFactor
			y = y * self.pixelScaleFactor
			g.fillRect(x, y,  self.pixelScaleFactor, self.pixelScaleFactor)




def main():


	frame = JFrame("Game of Life")

	pixelScaleFactor = 30;
	dimension = 25 
	seedLoad = 0.2

	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

	bounds = GraphicsEnvironment.getLocalGraphicsEnvironment().getMaximumWindowBounds()
	width = (dimension * pixelScaleFactor) + int(bounds.getX())
	height = (dimension * pixelScaleFactor) + int(bounds.getY())
	frame.setSize(width, height)
	frame.setResizable(False)

	grid = Grid(dimension, seedLoad, pixelScaleFactor)
	frame.getContentPane().add(grid)
	frame.show()

	# for i in range(0,10000):
	# 	time.sleep(0.05)
	# 	grid.repaint()


if __name__ == "__main__":
    main()