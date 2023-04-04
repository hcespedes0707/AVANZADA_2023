
def prim(start_node,graph):
    
    visited = set()
    
    
    mst = []
    
    
    visited.add(start_node)
    
    
    while len(visited) != len(graph):
        
        edges = []
        
       
        for node in visited:
            
            for edge in graph[node]:
                
                if edge[0] not in visited:
                    edges.append((node, edge[0], edge[1]))
        
      
        if len(edges) == 0:
           return mst
        
        
        min_edge = min(edges, key=lambda x: x[2])
        
       
        mst.append(min_edge)
        visited.add(min_edge[1])
       
    
    return mst



graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 4)],
    'D': [('A', 5), ('B', 1), ('C', 4)]
}

start_node = 'B'
mst = prim(start_node,graph)

print(mst)