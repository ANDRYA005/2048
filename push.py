import util

#grid = [[2,3,2,8],[2,0,0,8],[2,16,0,128],[0,2,2,0]]
#util.print_grid (grid)


def push_up (grid):
    """merge grid values upwards"""
    first_column = []
    second_column = []
    third_column = []
    fourth_column = []
    for i in range (4):
        first_column.append(grid[i][0])
        second_column.append(grid[i][1])
        third_column.append(grid[i][2])
        fourth_column.append(grid[i][3])
   
    zeros = first_column.count(0)
    for k in range (zeros):
        first_column.remove(0)
        first_column.append(0)
    for l in range(3):
        if first_column[l] == first_column[l+1] and first_column[l] != 0:
            first_column[l] = first_column[l] + first_column[l+1]
            del first_column[l+1]
            first_column.append(0)
    
    zeros = second_column.count(0)
    for k in range (zeros):
        second_column.remove(0)
        second_column.append(0)
    for l in range(3):
        if second_column[l] == second_column[l+1] and second_column[l] != 0:
            second_column[l] = second_column[l] + second_column[l+1]
            del second_column[l+1]
            second_column.append(0)           
    
    zeros = third_column.count(0)
    for k in range (zeros):
        third_column.remove(0)
        third_column.append(0)
    for l in range(3):
        if third_column[l] == third_column[l+1] and third_column[l] != 0:
            third_column[l] = third_column[l] + third_column[l+1]
            del third_column[l+1]
            third_column.append(0)           
        
    zeros = fourth_column.count(0)
    for k in range (zeros):
        fourth_column.remove(0)
        fourth_column.append(0)
    for l in range(3):
        if fourth_column[l] == fourth_column[l+1] and fourth_column[l] != 0:
            fourth_column[l] = fourth_column[l] + fourth_column[l+1]
            del fourth_column[l+1]
            fourth_column.append(0)           
    #print(fourth_column)    
    for m in range(4):
        grid[m] = [first_column[m]] + [second_column[m]] + [third_column[m]] + [fourth_column[m]]
    return grid     
#print(push_up(grid))

def push_down (grid):
    """merge grid values downwards"""
    first_column = []
    second_column = []
    third_column = []
    fourth_column = []
    for i in range (3,-1,-1):
        first_column.append(grid[i][0])
        second_column.append(grid[i][1])
        third_column.append(grid[i][2])
        fourth_column.append(grid[i][3])
    #first_column = first_column[::-1]
    #second_column = second_column[::-1] 
    #third_column = third_column[::-1] 
    #fourth_column = fourth_column[::-1] 
    zeros = first_column.count(0)
    for k in range (zeros):
        first_column.remove(0)
        first_column.append(0)
    for l in range(3):
        if first_column[l] == first_column[l+1] and first_column[l] != 0:
            first_column[l] = first_column[l] + first_column[l+1]
            del first_column[l+1]
            first_column.append(0)
    
    zeros = second_column.count(0)
    for k in range (zeros):
        second_column.remove(0)
        second_column.append(0)
    for l in range(3):
        if second_column[l] == second_column[l+1] and second_column[l] != 0:
            second_column[l] = second_column[l] + second_column[l+1]
            del second_column[l+1]
            second_column.append(0)           
    
    zeros = third_column.count(0)
    for k in range (zeros):
        third_column.remove(0)
        third_column.append(0)
    for l in range(3):
        if third_column[l] == third_column[l+1] and third_column[l] != 0:
            third_column[l] = third_column[l] + third_column[l+1]
            del third_column[l+1]
            third_column.append(0)           
        
    zeros = fourth_column.count(0)
    for k in range (zeros):
        fourth_column.remove(0)
        fourth_column.append(0)
    for l in range(3):
        if fourth_column[l] == fourth_column[l+1] and fourth_column[l] != 0:
            fourth_column[l] = fourth_column[l] + fourth_column[l+1]
            del fourth_column[l+1]
            fourth_column.append(0)               
    #print(fourth_column)
    for m in range(4):
            grid[m] = [first_column[-(m+1)]] + [second_column[-(m+1)]] + [third_column[-(m+1)]] + [fourth_column[-(m+1)]]
    #util.print_grid(grid)
    return grid     
#print(push_down (grid))

    
def push_left (grid):
    """merge grid values left"""
    counter = 0
    for rows in grid:
        zeros = rows.count(0)
        for k in range (zeros):
            rows.remove(0)
            rows.append(0)
        for l in range(3):
            if rows[l] == rows[l+1] and rows[l] != 0:
                rows[l] = rows[l] + rows[l+1]
                del rows[l+1]
                rows.append(0)
        grid[counter] = rows
        counter+=1
    return grid
#print(push_left (grid)) 


def push_right (grid):
    """merge grid values right"""
    counter = 0
    for rows in grid:
        rows = rows[::-1]
        zeros = rows.count(0)
        for k in range (zeros):
            rows.remove(0)
            rows.append(0)
        for l in range(3):
            if rows[l] == rows[l+1] and rows[l] != 0:
                rows[l] = rows[l] + rows[l+1]
                del rows[l+1]
                rows.append(0)
        grid[counter] = rows[::-1]
        counter+=1
    return grid
#print(push_right (grid))