multiline
!embed
<drac2>
args = &ARGS&
title = ""
desc = ""
footer = ""
image = ""


# This maze generation algorithm uses Kruskal's Algorithm, with cells as nodes and walls as initial edges. The resulting list of edges in the minimum spanning tree will represent the open paths between cells

# The maze's max x and y values/width and length
MAX_X = 15
MAX_Y = 15

# A factor affecting the frequency of loops being introduced into the maze. A lower value (minimum 1) increases the frequency of loops
LOOP_NEGATION_FACTOR = 25

# Create a matrix of cells along with their ranks
cells = [[(x,y) for y in range(MAX_Y)] for x in range(MAX_X)]
ranks = [[0 for y in range(MAX_Y)] for x in range(MAX_X)]

# Create a list of all walls
walls = []
for x in range(MAX_X):
    for y in range(MAX_Y):
        if x < MAX_X-1:
            walls.append(((x, y), (x+1, y)))
        if y < MAX_Y-1:
            walls.append(((x, y), (x, y+1)))
            
# Create two matrices to store corridors between cells. A 0 value indicates the corridor is blocked by a wall, a 1 value indicates it is open
horizontal_corridors = [[0 for y in range(MAX_Y)] for x in range(MAX_X-1)]
vertical_corridors = [[0 for y in range(MAX_Y-1)] for x in range(MAX_X)]

e = 0   # Number of walls removed/open corridors

while e < (MAX_X * MAX_Y) - 1:
    (x1, y1), (x2, y2) = walls.pop(randint(0, (len(walls)-1)))
    
    # Find parents of the two cells separated by the wall
    cell = (x1, y1)
    parent1 = cells[x1][y1]
    
    while parent1 != cell:
        cell = cells[cell[0]][cell[1]]
        parent1 = cells[cell[0]][cell[1]]
        
    cell = (x2, y2)
    parent2 = cells[x2][y2]
    while parent2 != cell:
        cell = cells[cell[0]][cell[1]]
        parent2 = cells[cell[0]][cell[1]]
        
    # Perform union if cells are of different trees using union by rank
    if parent1 != parent2:
        e += 1
        if x1 != x2:
            horizontal_corridors[x1][y1] = 1
        else:
            vertical_corridors[x1][y1] = 1
        if ranks[parent1[0]][parent1[1]] < ranks[parent2[0]][parent2[1]]:   # If rank of parent1 < rank of parent2
            cells[parent1[0]][parent1[1]] = parent2
        elif ranks[parent2[0]][parent2[1]] < ranks[parent1[0]][parent1[1]]: # If rank of parent2 < rank of parent1
            cells[parent2[0]][parent2[1]] = parent1
        else:
            cells[parent2[0]][parent2[1]] = parent1
            ranks[parent1[0]][parent1[1]] += 1
            
    elif randint(0,LOOP_NEGATION_FACTOR)<1:
        if x1 != x2:
            horizontal_corridors[x1][y1] = 1
        else:
            vertical_corridors[x1][y1] = 1
            
desc += "```"
for y in range(MAX_Y):
    for x in range(MAX_X):
        desc += "██"
        if x < MAX_X-1:
            if horizontal_corridors[x][y] == 1:
                desc += "■■"
            else:
                desc += "  "
    desc += "\n"
    if y < MAX_Y-1:
        for x in range(MAX_X):
            if vertical_corridors[x][y] == 1:
                desc += "▐▌  " if x < MAX_X-1 else "▐▌"
            else:
                desc += "    " if x < MAX_X-1 else "  "
    desc += "\n"

desc += "```"    
return f""" -title "{title}" -desc "{desc}" -footer "{footer}" -image "{image}" """
</drac2>
