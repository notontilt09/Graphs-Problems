"""
Given the starting position and the finishing position of a knight on a 8x8 chessboard, return the minimum
amount of moves necessary for the knight to travel from the startpoint to the endpoint.  The starting and ending position
will be given as tuples in the form (2, 1), (5, 8) for example.

A knight moves in the following pattern (2 squares in 1 direction, and then one square in the perpendicular direction)

In the figure below, a knight at point K, can move to any of the possible points labelled P.

1  0 0 0 0 0 0 0 0
2  0 0 P 0 P 0 0 0
3  0 P 0 0 0 P 0 0
4  0 0 0 K 0 0 0 0
5  0 P 0 0 0 P 0 0
6  0 0 P 0 P 0 0 0
7  0 0 0 0 0 0 0 0
8  0 0 0 0 0 0 0 0
   
   1 2 3 4 5 6 7 8

There is always a path from the start to the finish.
"""
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def bfs(starting_vertex, destination_vertex, graph):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue holding paths this time
        q = Queue()
        # empty set for visited vertexes
        visited = set()

        # enqueue a list representing path to starting_vertex which is just itself
        q.enqueue([starting_vertex])

        # while the queue isn't empty
        while q.size() > 0:
          # dequeue path
          v = q.dequeue()
          # node is the last vertex in path
          node = v[-1]

          # if we haven't visited node yet
          if node not in visited:
            # loop through neighbors
            for neighbor in graph[node]:
              # add neighbor to path
              path = list(v)
              path.append(neighbor)
              # enqueue the path for more searching
              q.enqueue(path)
              # if neighbor is goal, return the path
              if neighbor == destination_vertex:
                return path
            
            # add vertex to visited after we've searched it
            visited.add(node)

def knight_moves(start, finish):
  # lets build a graph of every square, and the possible squares that a knight can move from that square
  graph = {}

  # create the vertices of our graph, 1 for each square on the chessboard initialzed to an empty set
  for i in range(1, 9):
    for j in range(1, 9):
      graph[(i, j)] = set()

  # fill the empty sets with the potentital squares we can move from that square
  for square in graph:
    # 8 possible moves from each point, make sure each point within the bounds of the board
    # if so, add that move to the square's set
    x = square[0]
    y = square[1]
    # up2/right1
    if x < 8 and y < 7:
      graph[square].add((x+1, y+2))
    # up2/left1
    if x > 1 and y < 7:
      graph[square].add((x-1, y+2))
    # up1/right2
    if x < 7 and y < 8:
      graph[square].add((x+2, y+1))
    # up1/left2
    if x > 2 and y < 8:
      graph[square].add((x-2, y+1))
    # down2/right1
    if x < 8 and y > 2:
      graph[square].add((x+1, y-2))
    # down2/left1
    if x > 1 and y > 2:
      graph[square].add((x-1, y-2))
    # down1/right2
    if x < 7 and y > 1:
      graph[square].add((x+2, y-1))
    # down1/left2
    if x > 2 and y > 1:
      graph[square].add((x-2, y-1))
  
  # print(graph)

  # do a BFS from start to finish to find the shortest path, return the length of that path
  path = bfs(start, finish, graph)
  print(path)
  # subtract 1 from len(path) since bfs path includes start node
  return len(path) - 1


  
  


print(knight_moves((1, 1), (8, 8)))



  



