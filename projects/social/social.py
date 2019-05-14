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

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # use BFT to find all connected components of the userId
        q = Queue()
        # Create an empty Visited set
        connected = set()
        # Add the starting vertex to the queue
        q.enqueue(userID)
        # While the queue is not empty...
        while q.size() > 0:
          # Dequeue the first vertex
          v = q.dequeue()
          # If it has not been visited...
          if v not in connected:
            # Mark it as visited (print it and add it to the visited set)
            connected.add(v)
            # Then enqueue each of its neighbors in the queue
            for neighbor in self.friendships[v]:
              q.enqueue(neighbor)

        # use BFS to find shortest path to each component


        for user in connected:
          q = Queue()
        # empty set for seen vertexes
          seen = set()

        # enqueue a list representing path to useID which is just itself
          q.enqueue([userID])

        # while the queue isn't empty
          while q.size() > 0:
            # dequeue path
            v = q.dequeue()
            # node is the last vertex in path
            node = v[-1]

            # if we haven't visited node yet
            if node not in seen:
              # if the node is the destination
              if node == user:
                # add the key value pair to the visited dictionary
                visited[user] = v
              # loop through neighbors
              for neighbor in self.friendships[node]:
                # add neighbor to path
                path = list(v)
                path.append(neighbor)
              # enqueue the path for more searching
                q.enqueue(path)
            
            # add vertex to visited after we've searched it
              seen.add(node)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
