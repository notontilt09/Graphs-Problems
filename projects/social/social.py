import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i+1}')

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        random.shuffle(possibleFriendships)

        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def bfs(self, start, finish, graph):
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
        q.enqueue([start])

        # while the queue isn't empty
        while q.size() > 0:
          # dequeue path
          v = q.dequeue()
          # node is the last vertex in path
          node = v[-1]

          if node == finish:
              return [node]

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
              if neighbor == finish:
                return path
            
            # add vertex to visited after we've searched it
            visited.add(node)

        return None

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """


        # q = Queue()
        # # empty dict for seen vertexes
        # visited = {}

        # # enqueue a list representing path to userID which is just itself
        # q.enqueue([userID])

        # # while the queue isn't empty
        # while q.size() > 0:
        #   # dequeue path
        #   v = q.dequeue()
        #   # node is the last vertex in path
        #   node = v[-1]

        #   # if we haven't visited node yet
        #   if node not in visited:
        #       # add the key value pair to the visited dictionary
        #     visited[node] = v
        #     # loop through neighbors
        #     for neighbor in self.friendships[node]:
        #       # add neighbor to path
        #       path = list(v)
        #       path.append(neighbor)
        #     # enqueue the path for more searching
        #       q.enqueue(path)
          
        #   # add vertex to visited after we've searched it
        # return visited

        paths = {}

        for user in self.users:
            paths[user] = self.bfs(userID, user, self.friendships)
        
        paths = {path: paths[path] for path in paths if paths[path] is not None}
        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print('\n')
    total = 0
    for key in connections:
      total += len(connections[key])
    avg_separation = total / len(connections)
    print(avg_separation)




