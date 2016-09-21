# Bennett Alex Myers
# CS 2050 - Homework 4
# 4 April 2016

# Lee & Hubbard Section 7.9 Problem 5:
#     Not every graph must be represented explicitly. Sometimes it is just as
#     easy to write a function that given a vertex, will compute the vertices
#     that are adjacent to it (have edges between them). For instance, consider
#     the water bucket problem. There are two buckets in this problem: a 3 
#     gallon bucket and a 5 gallon bucket. The rules of the game say that you 
#     completely fill a bucket of water, you can pour one bucket into another,
#     and you can completely dump a bucket out on the ground. You cannot 
#     partially fill up a bucket, but you can pour one bucket into another. You
#     are to write a program that tells you how to start with two empty buckets
#     and end with 4 gallons in the 5 gallon bucket.
#     To complete this problem you must implement depth first search of a graph.
#     The vertices in this problem consist of the state of the problem which is
#     given by the amount of water in each bucket. Along with the search 
#     algorithm you must also implement an adjacent function that given a vertex
#     containing this state information will return a list of states that may be
#     adjacent to it.
#     The program should print out the list of actions to take to get from no 
#     water in either bucket to four gallons in the five gallon pail.
        
# Find the states adjacent to the given state.
def adjacent((state, prev, transition)):
    adj = {}
    
    # Dump out the 3-gallon bucket.x  
    s1 = (0,state[1])
    if not s1 in adj.keys():
        adj[s1] = "Dump out the 3-gallon bucket."
    
    # Dump out the 5-gallon bucket.
    s2 = (state[0],0)
    if not s2 in adj.keys():
        adj[s2] = "Dump out the 5-gallon bucket."
    
    # Fill the 3-gallon bucket.
    s3 = (3,state[1])
    if not s3 in adj.keys():
        adj[s3] = "Fill the 3-gallon bucket."
    
    # Fill the 5-gallon bucket.
    s4 = (state[0],5)
    if not s4 in adj.keys():
        adj[s4] = "Fill the 5-gallon bucket."
    
    total = state[0] + state[1]
    
    # Pour the 3-gallon bucket into the 5-gallon bucket.
    if total <= 5:
        s5 = (0,total)
    else:
        overflow = total - 5
        s5 = (overflow, 5)
    if not s5 in adj.keys():
        adj[s5] = "Pour the 3-gallon bucket into the 5-gallon bucket."
    
    # Pour the 5-gallon bucket into the 3-gallon bucket.
    if total <= 3:
        s6 = (total, 0)
    else:
        overflow = total - 3
        s6 = (3, overflow)
    if not s6 in adj.keys():
        adj[s6] = "Pour the 5-gallon bucket into the 3-gallon bucket."
        
    # Return a dictionary which maps the set of states adjacent from the given
    # state to the action necessary to transition to the adjacent state.
    return adj

# Path search algorithm.        
def findPath(start,goal):
    
    # Stack maintains states to visit as three-tuples consisting of the state,
    # its parent in the search, and the transition taken to get there.
    stack = []
    
    # Visited maps the visited states to an ordered pair consisting of its
    # parent state and the transition taken to get there.
    visited = {}
    
    stack.append((start,None,"Start state."))
            
    # Main loop. Performs a depth-first search using a stack to backtrack.
    while not stack == []:
        current = stack.pop()
        visited[current[0]] = (current[1],current[2])
        
        # Determine the path by recursively appending states and their parents.
        if current[0] == goal:
            node = current
            path = [(node[0],node[2])]
            while not node[1] == None:
                node = node[1]
                path.append((node[0],node[2]))
                
            path.reverse()
            return path
        
        # For each state in the current state's adjacency list, check to see if
        # that state has already been visited. If not, push it onto the stack.
        for s,a in adjacent(current).items():
            if not s in visited.keys():
                stack.append((s,current,a))
                
    # Return false if no path exists.
    return False

# Main program.

# States object maps buckets states to their previous states as determined by
# the path-searching algorithm. Previous states initialized to None.
states = {}

# Populate states with every possible combination of buckets (including ones
# unreachable from (0,0)).
for i in range(0,4):
    for j in range(0,6):
        states[(i,j)] = None
        
# Find a path from the initial state (0,0) (corresponding to two empty buckets)
# to (0,4) (corresponding to the state in which the 5-gallon bucket has 4
# gallons in it).
# Note: (1,4) and (2,4) are unreachable states, and (3,4) is one step away from
# (0,4), so (0,4) is the solution of choice.
path = findPath((0,0),(0,4))

# Print out the list of actions necessary to get to the goal state in a user-
# friendly output.
pathStr = "Solution:\n\nState:      Action Taken from Previous State:\n\n"
for x in path:
    pathStr += str(x[0]) + "      " + str(x[1]) + "\n"
print(pathStr)    