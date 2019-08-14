# import queue for BFS later on
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

def earliest_ancestor(ancestors, starting_node):
    # instantiate graph
    graph = {}

    # build graph with parents below children.  Later we can BFS and find longest path to an ancestor and return that ancestor
    for pair in ancestors:
      if pair[1] not in graph:
        graph[pair[1]] = set()
      graph[pair[1]].add(pair[0])

    # instantiate queue
    q = Queue()
    # enqueue path to starting node
    q.enqueue([starting_node])

    # set up variables to track maximum path length so far and the earliest ancestor.
    # if we don't find earlier ancestor, we're returning -1, so initialize as so.
    max_len = 1
    earliest_ancestor = -1

    # BFS algorithm
    while q.size() > 0:
      path = q.dequeue()
      v = path[-1]

      # if we have equivalent path lengths between two ancestors, return the one with smaller value
      if (len(path) == max_len and v < earliest_ancestor):
        earliest_ancestor = v
        max_len = len(path)
      
      # if length of current path > max_len, update max_len and earliest ancestor
      if (len(path) > max_len):
        earliest_ancestor = v
        max_len = len(path)

      # if statement fixes key error
      if v in graph:
        # add paths to neighboring nodes to our queue
        for parent in graph[v]:
          path_copy = list(path)
          path_copy.append(parent)
          q.enqueue(path_copy)
    
    return earliest_ancestor


      
    

    
    
    
    
    
    
    

    
    
