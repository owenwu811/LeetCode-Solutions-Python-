

#841
#medium


#There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

#When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

#Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

#correct python3 solution:


#rooms = [[1],[2],[3],[]]

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True #[True, False, False, False]
        canvisit = 1
        stack = [0] #we have to start by visiting the room at index 0 in our sublist of lists [[1],[2],[3],[]], so [1]
        while stack:
            current = stack.pop() #starts as 0 because stack starts at [0] because we must start by visiting the 0th index room in our input list of lists first
            for key in rooms[current]: #rooms[0] = [1], so key = 1
                if not visited[key]: #if the room has not been visited yet aka visited[1] is False, which it is from [True, False, False, False] initially
                    stack.append(key) #we popped 0 off the stack, so stack is now [], but since index 1 in visited is False, we append 1 to our stack [1]
                    visited[key] = True #we have to mark room 1 as visited - [True, True, False, False]
                    canvisit += 1 #we have been able to visit another room
        return canvisit == n
