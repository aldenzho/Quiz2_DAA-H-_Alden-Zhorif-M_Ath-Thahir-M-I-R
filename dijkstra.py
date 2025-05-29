import heapq

def dijkstra(graph, start, goal):
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return [], float("inf")
