"""

BFS Algorithm

"""
#graph to be explored, implemented using dictionary

graph = {'A':['B','C','E'], 'B':['D','E'], 'E':['A','B','D'], 'D':['B','E'], 'C':['A','F','G'], 'F':['C'], 'G':['C']}

#function that visits all nodes of a graph using BFS approach

def BFS(graph,start):
    queue = [start] #include all nodes yet to be checked
    explored = [] #include all nodes already checked
    
    while queue: #execute while loop until the list "queue" is empty
        node=queue.pop(0) #gets first element of the list "queue"
        if node not in explored:
            explored.append(node) #add node to the list "explored"
            neighbours = graph[node] #assign neighbours of the node
            
            for n in neighbours:
                queue.append(n) #adds neighbours of the node to the list "queue"
    return explored

