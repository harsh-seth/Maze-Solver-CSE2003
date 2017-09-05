grid = """+-+-+-+-+-+-+-+-+-+-+
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
														# the maze here

#find_left function here
def find_left():
	if curr[0]==next_pos[0] and curr[1]<next_pos[1]:
		return (curr[0]-1,curr[1])

	if curr[1]==next_pos[1] and curr[0]<next_pos[0]:
		return (curr[0]+1,next_pos[1])

	if curr[0]==next_pos[0] and curr[1]>next_pos[1]:
		return (curr[0],curr[1]+1)

	if curr[1]==next_pos[1] and curr[0]>next_pos[0]:
		return (curr[0],next_pos[1]-1)


#find_right function here



#find charachter at given pos
def find_char(l, grid):
	return grid[l[0]][l[1]]

#move fron in the direction by one unit
def move_ahead(curr, next_pos, grid):
	grid[curr[0]][curr[1]] = 'o'
	temp = curr
	curr = next_pos
	if temp[0] == next_pos[0] and temp[1] == next_pos[1] - 1:		# move right ahead
		next_pos[1] = next_pos[1] + 1
	elif temp[0] == next_pos[0] and temp[1] == next_pos[1] + 1:		# 
		next_pos[1] = next_pos[1] - 1  
	elif temp[0] == next_pos[0] - 1 and temp[1] == next_pos[1]:
		next_pos[0] = next_pos[0] + 1
	elif temp[0] == next_pos[0] + 1 and temp[1] == next_pos[1]:
		next_pos[0] = next_pos[0] - 1
	return curr, next_pos


wall_chars = "+-|_"
start = ( ,)													#Enter start point here
grid[start[0], start[1]] = 'S'
end = ( ,)														#Enter end point here
endchar = grid[end[0], end[1]] = 'E'


curr = start
next_pos = !curr[0]? (curr[0], curr[1]+1) : (curr[0]+1, curr[1])

lchar = find_char(find_left(curr, next_pos), grid)
rchar = find_char(find_right(curr, next_pos), grid)


while (endchar not in [find_char(next_pos), lchar, rchar]):
	lchar = find_char(find_left(curr, next_pos), grid)
	rchar = find_char(find_right(curr, next_pos), grid)
	if lchar not in wall_chars: 									# left wall empty
		next_pos = find_left(curr, next_pos)
	elif find_char(next_pos) not in wall_chars:
		curr, next_pos = move_ahead(curr, next_pos, grid)
	else:
		next_pos = find_right(curr, next_pos)
	# grid[curr[0]][curr[1]] = 'o'

p = "\n".join(["".join(i) for i in grid])
print(p)
		

