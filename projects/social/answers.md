### 1. To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?

500 times.  Because of the bidirectional nature of friendships, we only need to call add friendship (num_users * avg_friends // 2)

### 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?

Almost 100% of users will be in a particular user's extended network.  Kevin Bacon theorem.

Adding the following code to the run method gives us the average separation between two users, assuming a direct friendship is 1 degree
```python
total = 0
for key in connections:
  total += len(connections[key]) - 1
avg_separation = total / len(sg.users)
print(avg_separation)
```

Running this a few times gave an average separation of about 4.5 degrees.  Not quite Kevin Bacon Theorem.