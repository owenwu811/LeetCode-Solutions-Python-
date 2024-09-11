

#841
#medium


#There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

#When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

#Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

#correct python3 solution:

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        canvisit = 1
        stack = [0] #we have to start by visiting the room at index 0 in our sublist of lists [[1],[2],[3],[]], so [1]
        while stack:
            current = stack.pop()
            for key in rooms[current]: #rooms[0] = [1], so key = 1
                if not visited[key]: #if the room has not been visited yet aka visited[1] is False
                    stack.append(key)
                    visited[key] = True #we have to mark it as visited
                    canvisit += 1
        return canvisit == n
