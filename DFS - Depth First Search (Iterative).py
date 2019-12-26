"""

DFS Algorithm

"""
#graph to be explored, implemented using dictionary
g = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}

#function that visits all nodes of a graph using DFS (Iterative) approach
def DFS(graph,start):
    stack = [start] #add nodes yet to be checked
    explored = [] #add nodes already checked
    
    while stack: #execute while loop until the list "stack" is empty
        node = stack.pop() #gets first element of the list "stack"
        if node not in explored:
            explored.append(node) #add node to the list "explored"
            neighbours = graph[node] #assign neighbours of the node
            
        for n in reversed(neighbours):
            if n not in explored:
                stack.append(n) #adds neighbours of the node to the list "queue"
    return explored            
    
print(DFS(g,'A'))
                
            