"""

DFS Algorithm

"""

g = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}

def DFS(graph,start):
    stack = [start]
    explored = []
    
    while stack:
        node = stack.pop()
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
            
        for n in reversed(neighbours):
            if n not in explored:
                stack.append(n)
    return explored            
    
                
            