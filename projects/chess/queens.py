"""
Given a list of starting positions of 8 queens on an 8x8 chessboard, determine if any of the queens are attacking each
other.  If they are, return the position first queen in the list which is in an attacking position.  Otherwise, 
return the string 'True'.
"""

def EightQueens(strArr):
    graph = {}
    
    # creating graph where keys are starting positions of the 8 queens, and values will be set of all squares they can hit
    for position in strArr:
        graph[position] = set()
    

    for position in graph:
        # adding horizontal positions the queens can hit
        for i in range(1, 9):
          if int(position[1]) != i:
            graph[position].add(f"({i},{int(position[3])})")
        # # adding vertical positions the queens can hit
        for j in range(1, 9):
          if int(position[3]) != j:
            graph[position].add(f"({int(position[1])},{j})")
        # adding all Northeast diagonal positions the queens can hit
        # grab x, y coordinates and add all squares until we hit an edge
        x = int(position[1])
        y = int(position[3])
        while x <= 7 and y <= 7:
          x += 1
          y += 1
          graph[position].add(f"({x},{y})")
        # adding all NorthWest diagonal positions the queens can hit
        # grab x, y coordinates and add all squares until we hit an edge
        x = int(position[1])
        y = int(position[3])
        while x >= 2 and y <= 7:
          x -= 1
          y += 1
          graph[position].add(f"({x},{y})")
        # adding all SouthEast diagonal positions the queens can hit
        # grab x, y coordinates and add all squares until we hit an edge
        x = int(position[1])
        y = int(position[3])
        while x <= 7 and y >= 2:
          x += 1
          y -= 1
          graph[position].add(f"({x},{y})")
        # adding all SouthWest diagonal positions the queens can hit
        # grab x, y coordinates and add all squares until we hit an edge
        x = int(position[1])
        y = int(position[3])
        while x >= 2 and y >= 2:
          x -= 1
          y -= 1
          graph[position].add(f"({x},{y})")
    

    # print(graph)


    

    for position in strArr:
      for square in graph[position]:
        if square in graph:
          return position
    
    return 'True'


print(EightQueens(["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]))