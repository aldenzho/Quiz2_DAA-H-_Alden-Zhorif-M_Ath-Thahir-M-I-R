import heapq
import math

def heuristic(a, b, positions):
    x1, y1 = positions[a]
    x2, y2 = positions[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def astar(graph, start, goal, positions):
    queue = []
    heapq.heappush(queue, (0, [start]))
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        current = path[-1]

        if current == goal:
            return path, cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                g = sum(graph[new_path[i]].__getitem__([v for v, _ in graph[new_path[i]]].index(new_path[i+1]))[1] for i in range(len(new_path) - 1))
                h = heuristic(neighbor, goal, positions)
                heapq.heappush(queue, (g + h, new_path))

    return None, float('inf')


