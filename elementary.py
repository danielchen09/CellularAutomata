from PIL import Image

class CA:
	def __init__(self, length, rule, generations=0):
		if generations:
			self.generations = generations
		else:
			self.generations = length

		self.length = length
		self.rule = rule
		self.ruleset = list('{0:08b}'.format(self.rule))

		self.grid = []

		cells = ['0']*length
		cells[length//2] = '1'
		self.grid.append(cells)


		for generation in range(self.generations):
			newcells = ['0']
			for i in range(1, len(cells) - 1):
				newcells.append(self.getState(cells[i-1:i+2]))
			newcells.append('0')
			cells = newcells
			self.grid.append(cells)


	def getState(self, neighbors):
		return self.ruleset[7 - int(''.join(neighbors), 2)]

	def show(self, show=True):
		unit = 5
		w = unit*self.length
		h = unit*self.generations

		im = Image.new('RGB', (w, h))
		for x in range(w):
			for y in range(h):
				im.putpixel((x, y), tuple([int(self.grid[y//unit][x//unit])*255]*3))

		if show:
			im.show()

		return im

def saveGIF(start, end):
	frames = []
	for i in range(0, 256):
		ca = CA(100, i, 100)
		frames.append(ca.show(0))
	frames[0].save('elementary.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)

if __name__ == '__main__':
	ca = CA(100, 57, 100)
	ca.show(1)