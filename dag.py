def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = [u for u in graph if in_degree[u] == 0]
    result = []
    
    while queue:
        u = queue.pop(0)
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(result) != len(graph):
        raise ValueError("Graph has a cycle")
    
    return result
