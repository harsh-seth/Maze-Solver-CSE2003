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


block = ["+","|","-"]
path = [" "]
end = ["E"]
start = ["S"]


def find_left():
	if current[0][0]==current[1][0] and current[0][1]<current[1][1]:
		return (current[0][0]-1,current[0][1])

	if current[0][1]==current[1][1] and current[0][0]<current[1][0]:
		return (current[0][0]+1,current[1][1])

	if current[0][0]==current[1][0] and current[0][1]>current[1][1]:
		return (current[0][0],current[0][1]+1)

	if current[0][1]==current[1][1] and current[0][0]>current[1][0]:
		return (current[0][0],current[1][1]-1)

def pos((x,y)):
	return grid[x][y]

current = [(2,0),(2,1)]
print(find_left(),pos(find_left()))
current = [(4,5),(5,5)]	
print(find_left(),pos(find_left()))
current = [(5,5),(4,5)]
print(find_left(),pos(find_left()))
current = [(2,1),(2,0)]
print(find_left(),pos(find_left()))



	