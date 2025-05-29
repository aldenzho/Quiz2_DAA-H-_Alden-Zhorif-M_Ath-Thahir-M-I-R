import time
from bfs import bfs
from dag import topological_sort
import prim  
from astar import astar
from kruskal import kruskal

def input_unweighted_graph():
    graph = {}
    n = int(input("Number of nodes (unweighted graph): "))
    for _ in range(n):
        node = input("Node name: ")
        neighbors = input(f"Neighbors of {node} (comma-separated): ").split(",")
        graph[node] = [nbr.strip() for nbr in neighbors if nbr.strip()]
    return graph

def input_weighted_graph():
    graph = {}
    edges = []
    n = int(input("Number of edges (weighted graph): "))
    for _ in range(n):
        u, v, w = input("Edge (format: node1 node2 weight): ").split()
        w = int(w)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected
        edges.append((u, v, w))
    return graph, edges

def input_node_positions(nodes):
    positions = {}
    print("\nEnter positions for each node (format: x y):")
    for node in nodes:
        x, y = map(float, input(f"Position of {node}: ").split())
        positions[node] = (x, y)
    return positions

def run_unweighted():
    print("\n=== Input Unweighted Graph ===")
    graph = input_unweighted_graph()
    start_node = input("Start node for BFS: ")
    goal_node = input("Goal node for BFS: ")

    # Run BFS
    start = time.time()
    bfs_path = bfs(graph, start_node, goal_node)
    bfs_time = time.time() - start

    # Run Topological Sort
    start = time.time()
    topo_order = topological_sort(graph)
    topo_time = time.time() - start

    # Output
    print("\n--- Result for Unweighted Graph ---")
    print(f"BFS Path {start_node} -> {goal_node}: {bfs_path} (time: {bfs_time:.6f}s)")
    print(f"Topological Sort Order: {topo_order} (time: {topo_time:.6f}s)")

def run_weighted():
    print("\n=== Input Weighted Graph ===")
    graph, edges = input_weighted_graph()
    prim_start = input("Start node for Prim: ")
    astar_start = input("Start node for A*: ")
    astar_goal = input("Goal node for A*: ")

    # Input node positions (for A*)
    positions = input_node_positions(graph.keys())

    # Run Prim
    start = time.time()
    prim_result = prim.prim(graph, prim_start)

    prim_time = time.time() - start

    # Run Kruskal
    start = time.time()
    nodes = list(graph.keys())
    kruskal_result = kruskal(nodes, edges)
    kruskal_time = time.time() - start

    # Run A*
    start = time.time()
    astar_path, astar_cost = astar(graph, astar_start, astar_goal, positions)
    astar_time = time.time() - start

    # Output
    print("\n--- Result for Weighted Graph ---")
    print(f"Prim MST from {prim_start}: {prim_result} (time: {prim_time:.6f}s)")
    print(f"Kruskal MST: {kruskal_result} (time: {kruskal_time:.6f}s)")
    print(f"A* Path {astar_start} -> {astar_goal}: {astar_path} (cost: {astar_cost}, time: {astar_time:.6f}s)")

# --- MAIN MENU ---

def main():
    print("=== Graph Algorithm Comparison ===")
    print("1. Unweighted Graph (BFS & Topological Sort)")
    print("2. Weighted Graph (Prim, Kruskal & A*)")
    choice = input("Choose graph type [1/2]: ")

    if choice == '1':
        run_unweighted()
    elif choice == '2':
        run_weighted()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



'''
==================OPSI TAMBAHAN FITUR=========================

# visualiassi MST
print("\n=== Input Weighted Graph for MST (Prim & Kruskal) ===")
weighted_graph, edges = input_weighted_graph()
prim_start = input("Start node for Prim's algorithm: ")

start = time.time()
mst_prim = prim.prim(weighted_graph, prim_start)  # panggil fungsi prim dari modul prim
end = time.time()

total_cost_prim = sum(w for _, _, w in mst_prim)

print("Prim-Jarnik MST edges and weights:")
for u, v, w in mst_prim:
    print(f"{u} - {v}: {w}")
print(f"Total cost: {total_cost_prim}, time: {end - start:.6f} seconds")

positions = prim.input_positions_and_visualize(weighted_graph.keys(), mst_prim)

'''

'''
=== Input Unweighted Graph for BFS and DAG ===
Number of nodes (unweighted graph): 6
Node name: A
Neighbors of A (comma-separated): B,C
Node name: B
Neighbors of B (comma-separated): D
Node name: C
Neighbors of C (comma-separated): D,E
Node name: D
Neighbors of D (comma-separated): F
Node name: E
Neighbors of E (comma-separated): F
Node name: F
Neighbors of F (comma-separated): 
Start node for BFS: A
Goal node for BFS: F
 

'''

'''
=== Input Weighted Graph for MST (Prim & Kruskal) ===
Number of edges (weighted graph): 7
Edge (format: node1 node2 weight): A B 4
Edge (format: node1 node2 weight): A C 3
Edge (format: node1 node2 weight): B D 5
Edge (format: node1 node2 weight): C D 6
Edge (format: node1 node2 weight): C E 2
Edge (format: node1 node2 weight): D F 1
Edge (format: node1 node2 weight): E F 4
Start node for Prim's algorithm: A

'''

''' 
==============input for Astar===============

=== Input Weighted Graph for MST (Prim & Kruskal) ===
Number of edges (weighted graph): 5
Edge (format: node1 node2 weight): A B 3
Edge (format: node1 node2 weight): A C 4
Edge (format: node1 node2 weight): B D 2
Edge (format: node1 node2 weight): C D 5
Edge (format: node1 node2 weight): D E 1

Start node for Prim's algorithm: A

=== A* Search ===
Start node for A*: A
Goal node for A*: E
Enter positions for each node (format: x y):
Position of A: 0 0
Position of B: 1 2
Position of C: 2 0
Position of D: 3 2
Position of E: 4 3

'''