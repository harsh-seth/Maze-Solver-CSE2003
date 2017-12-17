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



grid = """
++++++++++++++++++++++
S +       +   +   + ++
+ + +++++ +++ + + + ++
+ + +   +   + + +   ++
+ + + +++++ + + + ++++
+   + +     +   +   ++
+++++ + +++++ +++++ ++
+     + +   + +     ++
+ +++++ +++ + + ++++++
+   +   +     + +   ++
+++ + +++ + +++ + + ++
+         +   + + + ++
+ + +++ + +++++ + + ++
+ + +   +     +   + ++
+++ + +++ +++ +++++ ++
+   + + + + +       ++
+ +++ + + + + ++++++++
+   + +   + + +     ++
+++ + + +++ + + +++ ++
+     +     +   +    E
++++++++++++++++++++++
"""


grid = [list(row) for row in grid.splitlines()]


block = ["+","|","-","_","."]
path = [" ","o"]
end = ["E"]
start = ["S"]

curr =  (2,-1)
next_pos = (2,0)
last_next_pos = (2,-1)


def find_left():
	if curr[0]==next_pos[0] and curr[1]<next_pos[1]:
		return (curr[0]-1,next_pos[1])

	if curr[1]==next_pos[1] and curr[0]<next_pos[0]:
		return (curr[0]+1,next_pos[1]+1)

	if curr[0]==next_pos[0] and curr[1]>next_pos[1]:
		return (curr[0]+1,next_pos[1])

	if curr[1]==next_pos[1] and curr[0]>next_pos[0]:
		return (curr[0]-1,next_pos[1]-1)

def find_right():
	if curr[0]==next_pos[0] and curr[1]<next_pos[1]:
		return (curr[0]+1,next_pos[1])

	if curr[1]==next_pos[1] and curr[0]<next_pos[0]:
		return (curr[0]+1,next_pos[1]-1)

	if curr[0]==next_pos[0] and curr[1]>next_pos[1]:
		return (curr[0]-1,next_pos[1])

	if curr[1]==next_pos[1] and curr[0]>next_pos[0]:
		return (curr[0]-1,next_pos[1]+1)	

def move_ahead():
	if curr[0]==next_pos[0] and curr[1]<next_pos[1]:
		return (curr[0],next_pos[1]+1)

	if curr[1]==next_pos[1] and curr[0]<next_pos[0]:
		return (next_pos[0]+1,next_pos[1])

	if curr[0]==next_pos[0] and curr[1]>next_pos[1]:
		return (curr[0],next_pos[1]-1)

	if curr[1]==next_pos[1] and curr[0]>next_pos[0]:
		return (next_pos[0]-1,next_pos[1])

def pos(l):
	if grid[l[0]][l[1]] in block or grid[l[0]][l[1]] in end or grid[l[0]][l[1]] in path or grid[l[0]][l[1]] in start:
		return grid[l[0]][l[1]]

m = maze('maze1.txt')
m.drawmaze()
m.updatepos(m.startrow,m.startcol)
count = 0

i = 0
print(pos(move_ahead()))
while ((pos(move_ahead()) !='E') and (pos(find_right()) !='E') and (pos(find_left()) != 'E')):
	count += 1
	if ((pos(find_left()) =='S') or (pos(find_right()) =='S') or (pos(move_ahead()) == 'S')):
		print("\nYou shall not escape this!")
		break
	i=i+1
	last_next_pos = next_pos
	if pos(find_right()) in path:
		grid[next_pos[0]][next_pos[1]]="o"
		next_pos = find_right()
		if (grid[next_pos[0]][next_pos[1]]=="o"):
			grid[curr[0]][curr[1]]="."
			m.updatepos(last_next_pos[0],last_next_pos[1],tried)
		else:
			m.updatepos(next_pos[0],next_pos[1],partofpath)
	elif pos(move_ahead()) in path:
		grid[next_pos[0]][next_pos[1]]="o"
		next_pos = move_ahead()
		if (grid[next_pos[0]][next_pos[1]]=="o"):
			grid[curr[0]][curr[1]]="."
			m.updatepos(last_next_pos[0],last_next_pos[1],tried)
		
		else:
			m.updatepos(next_pos[0],next_pos[1],partofpath)
	elif pos(find_left()) in path:
		grid[next_pos[0]][next_pos[1]]="o"
		next_pos = find_left()
		if (grid[next_pos[0]][next_pos[1]]=="o"):
			grid[curr[0]][curr[1]]="."
			m.updatepos(last_next_pos[0],last_next_pos[1],tried)
		else:
			m.updatepos(next_pos[0],next_pos[1],partofpath)
	else:
		m.updatepos(next_pos[0],next_pos[1],tried)
		grid[next_pos[0]][next_pos[1]] = "."
		grid[curr[0]][curr[1]] = " "
		next_pos = curr
	
	curr=last_next_pos

print("\n".join("".join(row) for row in grid))
print("We checked the walls", count, "times.")
