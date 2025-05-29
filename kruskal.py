def kruskal(nodes, edges):
    parent = {node: node for node in nodes}
    
    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    mst = []
    edges.sort(key=lambda x: x[2])
    
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
    
    return mst
