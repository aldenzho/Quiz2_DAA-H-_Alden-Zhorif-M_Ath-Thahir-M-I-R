import heapq
import math
def heuristic(pos1, pos2):
    return math.dist(pos1, pos2)

def gbfs(graph, start, goal, positions):
    frontier = [(heuristic(positions[start], positions[goal]), start, [start])]
    visited = set()

    while frontier:
        _, current, path = heapq.heappop(frontier)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor, _ in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(frontier, (heuristic(positions[neighbor], positions[goal]), neighbor, path + [neighbor]))
    return[]