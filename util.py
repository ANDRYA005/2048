import copy

def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for y in range (4):
        grid.append([])
        for x in range(4):
            grid[y].append(0)
    return grid
    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+" + "-"*20 + "+")
    for rows in grid:
        print("|", end = "")
        for elements in rows:
            if elements == 0:
                print("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(elements),end="")
        print("|")
    print("+" + "-"*20 + "+")
#print_grid (grid)

def check_lost (grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    row_one = grid[0]
    row_two = grid[1]
    row_three = grid[2]
    row_four = grid[3]    
    for rows in grid: 
        if 0 in rows:
            return False
        elif not(0 in rows):
            for i in range(4):
                if row_one[i] == row_two[i] or row_two[i] == row_three[i] or row_three[i] == row_four[i]:
                    return False                
                elif i != 3: 
                    if rows[i] == rows[i+1]:
                        return False                  
    return True

#print(check_lost(grid))
                


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for rows in grid:
        for elements in rows:
            if elements >= 32:
                return True
    return False
#print(check_won(grid))            



def copy_grid (grid):
    """return a copy of the given grid"""
    grid_copy = copy.deepcopy(grid)    
    return grid_copy
#print(copy_grid(grid))



def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range (4):
        if grid1[i] != grid2[i]:
            return False
    return True
