# Data is formatted as a list of parent child pairs
# Each individual is assigned a unique interger indentifier

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor - the one at the farthest distance from the input individual.
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
# If the input individual has no parents, the function should return -1.

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    
    stack = Stack()
    stack.push([starting_node])
    
    visited = set()
    # print("visited", visited)
    # print("stack", stack)
    
    # Look for farthest distance from the starting node
    farthest_path = []
    
    while stack.size() > 0:
        path = stack.pop()
        print(path)
        
        
        
        
        
        if path[-1] not in visited:
            visited.add(path[-1])
            
            for pair in ancestors:
                if pair[1] == path[-1]:
                    #print(pair[1], path[-1])
                    new_path = [*path, pair[0]]
                    print("first", new_path)
                    #new_path.append(pair[0])
                    stack.push(new_path)
                    #print("new_path", new_path)
                    
    if starting_node == farthest_path[-1]:
            return -1    
        
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 9))