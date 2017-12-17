import turtle

partofpath='O'
tried='.'
obstacle='+'
deadend='-'

class maze:
	def __init__(self,mazefile):
		rowsinmaze=0
		colsinmaze=0
		self.mazelist=[]
		maze_file=open(mazefile,'r')
		rowsinmaze=0
		for line in maze_file:
			rowlist=[]
			col=0
			for ch in line[:-1]:
				rowlist.append(ch)
				if ch=='S'  :
					self.startrow=rowsinmaze
					self.startcol=col
				col+=1
			rowsinmaze+=1
			self.mazelist.append(rowlist)
			colsinmaze=len(rowlist)
		self.rowsinmaze=rowsinmaze
		self.colsinmaze=colsinmaze
		self.xtranslate=-colsinmaze/2
		self.ytranslate=rowsinmaze/2
		self.t=turtle.Turtle()
		self.t.shape('turtle')
		self.wn=turtle.Screen()
		self.wn.setworldcoordinates(-(colsinmaze-1)/2-0.5,-(rowsinmaze-1)/2-0.5,
									 (colsinmaze-1)/2,(rowsinmaze-1)/2)
	def drawmaze(self):
		self.t.speed(10000000000000000000)
		for y in range(self.rowsinmaze):
			for x in range(self.colsinmaze):
				if self.mazelist[y][x]==obstacle:
					self.drawcenteredbox(x+self.xtranslate,-y+self.ytranslate,'orange')
		self.t.color('black')
		self.t.fillcolor('blue')
		self.t.speed(1)

	def drawcenteredbox(self,x,y,color):
		self.t.up()
		self.t.goto(x-0.5,y-0.5)
		self.t.color(color)
		self.t.fillcolor(color)
		self.t.setheading(90)
		self.t.down()
		self.t.begin_fill()
		for i in range(4):
			self.t.forward(1)
			self.t.right(90)
		self.t.end_fill()

	def moveturtle(self,x,y):
		self.t.up()
		self.t.setheading(self.t.towards(x+self.xtranslate,-y+self.ytranslate))
		self.t.goto(x+self.xtranslate,-y+self.ytranslate)

	def dropbread(self,color):
		self.t.dot(10,color)

	def updatepos(self,row,col,val=None):
		if val:
			self.mazelist[row][col]=val
		self.moveturtle(col,row)
		if val==partofpath:
			color='green'
		elif val==obstacle:
			color='red'
		elif val==tried:
			color='black'
		else:
			color=None
		if color:
			self.dropbread(color)

	def isexit(self,row,col):
		return (row==0 or row==self.rowsinmaze-1 or col==0 or col==self.colsinmaze-1)
	
	def getitem(self,idx):
		return self.mazelist(idx)


m=maze('maze1.txt')
m.drawmaze()
m.updatepos(m.startrow,m.startcol)

grid = """
+-+-+-+-+-+-+-+-+-+-+
S |       |   |   | |
+ + +-+-+ +-+ + + + +
| | |   |   | | |   |
+ + + +-+-+ + + + +-+
|   | |     |   |   |
+-+-+ + +-+-+ +-+-+ +
|     | |   | |     |
+ +-+-+ +-+ + + +-+-+
|   |   |     | |   |
+-+ + +-+ + +-+ + + +
|         |   | | | |
+ + +-+ + +-+-+ + + +
| | |   |     |   | |
+-+ + +-+ +-+ +-+-+ +
|   | | | | |       |
+ +-+ + + + + +-+-+-+
|   | |   | | |     |
+-+ + + +-+ + + +-+ +
|     |     |   |   E
+-+-+-+-+-+-+-+-+-+-+
"""

g = [list(row) for row in grid.splitlines()]
count = 0
for i in range(len(g)):
	for j in range(len(g[i])):
		if g[i][j]=="S":
			start_x,start_y = i,j
		if g[i][j]=="E":
			end_x,end_y = i,j
start,end,visit,sol,path = "SE.o "

def search(x,y):
	global count
	count += 1
	if g[x][y] in (start,path):
		g[x][y] = visit
		m.updatepos(x,y,tried)
		if search(x,y+1) or search(x,y-1) or search(x+1,y) or search(x-1,y):
			g[x][y] = sol
			m.updatepos(x,y,partofpath)
			return True
	elif g[x][y] == end:
		return True
	return False

search(start_x,start_y)
print("\n".join("".join(row) for row in g))
print("We called", count, "recursions.")
