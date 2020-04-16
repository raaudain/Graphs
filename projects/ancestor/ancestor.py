# Data is formatted as a list of parent child pairs
# Each individual is assigned a unique interger indentifier

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor - the one at the farthest distance from the input individual.
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
# If the input individual has no parents, the function should return -1.

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    stack = Stack()
    stack.push([starting_node])
     
    farthest_path = []
    visited = set()
    
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        
        if vertex not in visited:
            visited.add(vertex)
            
            # Loops through parent/child pairs
            for pair in ancestors:
                parent = pair[0]
                child = pair[1]
                
                # Pushes path and parent to stack if child and vertex are equal
                if child == vertex:
                    temp_path = [*path, parent]                  
                    stack.push(temp_path)

        # Sets farthest_path as path if path's length is larger 
        # or the vertex is larger than the last node in farthest_path
        if len(path) > len(farthest_path) or vertex < farthest_path[-1]:
            farthest_path = path
    
    # If the input individual has no parents, return -1.       
    if starting_node == farthest_path[-1]:
            return -1    
    
    return farthest_path[-1]   



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))