def find_right(curr, next_pos):
        if curr[0] is next_pos[0]: # if in a vertical line
                if curr[1] < next_pos[1]: # if facing up
                        return((curr[0] + 1, curr[1]))
                else: # if facing down
                        return((curr[0] - 1, curr[1]))
        else: # if in a horizontal line
                if curr[0] < next_pos[0]: # if facing ahead
                        return((curr[0], curr[1] -1))
                else: # if facing behind
                        return((curr[0], curr[1] +1))

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(find_right((2,2),(3,2)))
