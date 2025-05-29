from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node, to_node):
        self.adj_list[from_node].append(to_node)
        self.adj_list[to_node].append(from_node)  # assume the graph is undirected

    def bfs(self, start, goal):
        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None
