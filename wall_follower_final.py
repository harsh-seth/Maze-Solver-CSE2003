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

i=0
print(pos(move_ahead()))
while ((pos(move_ahead()) !='E') and (pos(find_right()) !='E') and (pos(find_left()) != 'E')):
	if ((pos(find_left()) =='S') or (pos(find_right()) =='S') or (pos(move_ahead()) == 'S')):
		print("\nYou shall not escape this!")
		break
	i=i+1
	# print(i)
	last_next_pos = next_pos
	if pos(find_right()) in path:
		next_pos = find_right()
	elif pos(move_ahead()) in path:
		next_pos = move_ahead()
	elif pos(find_left()) in path:
		next_pos = find_left()
	else:
		grid[next_pos[0]][next_pos[1]] = "."
		grid[curr[0]][curr[1]] = " "
		next_pos = curr
		curr=last_next_pos

	curr=last_next_pos
	if (grid[next_pos[0]][next_pos[1]]=="o"):
		grid[curr[0]][curr[1]]="."
	grid[next_pos[0]][next_pos[1]]="o"

	# print(curr,next_pos,find_left(), find_right())
	#print("\n".join("".join(row) for row in grid))
	#print(curr,next_pos)

print("\n".join("".join(row) for row in grid))