"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
          self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
          self.vertices[v1].add(v2)
        else:
          raise IndexError('One or both of those vertices do not exist.')
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
          # Dequeue the first vertex
          v = q.dequeue()
          # If it has not been visited...
          if v not in visited:
            # Mark it as visited (print it and add it to the visited set)
            print(v)
            visited.add(v)
            # Then enqueue each of its neighbors in the queue
            for neighbor in self.vertices[v]:
              q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Push the starting vertex to the stack
        s.push(starting_vertex)
        # While the Stack is not empty...
        while s.size() > 0:
          # Pop the first vertex
          v = s.pop()
          # If it has not been visited...
          if v not in visited:
            # Mark it as visited (print it and add it to the visited set)
            print(v)
            visited.add(v)
            # Then push each of its neighbors onto the Stack
            for neighbor in self.vertices[v]:
              s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Mark the starting node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT_Recursive on each unvisited neighbors
        for neighbor in self.vertices[starting_vertex]:
          if neighbor not in visited:
            self.dft_recursive(neighbor, visited)
    def bfs(self, starting_vertex, destination_vertex):
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
            for neighbor in self.vertices[node]:
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

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create empty stack holding paths this time
        s = Stack()
        # empty set for visited vertexes
        visited = set()

        # enqueue a list representing path to starting_vertex which is just itself
        s.push([starting_vertex])

        # while the queue isn't empty
        while s.size() > 0:
          # dequeue path
          v = s.pop()
          # node is the last vertex in path
          node = v[-1]

          # if we haven't visited node yet
          if node not in visited:
            # loop through neighbors
            for neighbor in self.vertices[node]:
              # add neighbor to path
              path = list(v)
              path.append(neighbor)
              # enqueue the path for more searching
              s.push(path)
              # if neighbor is goal, return the path
              if neighbor == destination_vertex:
                return path
            
            # add vertex to visited after we've searched it
            visited.add(node)
        





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('vertices', graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\ndft')
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('\nbft')
    graph.bft(3)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\ndft_recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('\nbfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('\ndfs')
    print(graph.dfs(1, 6))
