import time
from bfs import bfs
from dfs import dfs
from dag import topological_sort
from astar import astar
from dijkstra import dijkstra
from gbfs import gbfs
from kruskal import kruskal
import prim

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
    start_node = input("Start node for BFS/DFS: ")
    goal_node = input("Goal node for BFS/DFS: ")

    # BFS
    start = time.time()
    path_bfs = bfs(graph, start_node, goal_node)
    bfs_time = time.time() - start

    # DFS
    start = time.time()
    path_dfs = dfs(graph, start_node, goal_node)
    dfs_time = time.time() - start

    # Output
    print("\n--- Result for Unweighted Graph ---")
    print(f"BFS Path {start_node} -> {goal_node}: {path_bfs} (time: {bfs_time:.6f}s)")
    print(f"DFS Path {start_node} -> {goal_node}: {path_dfs} (time: {dfs_time:.6f}s)")

def run_weighted():
    print("\n=== Input Weighted Graph ===")
    graph, edges = input_weighted_graph()
    positions = input_node_positions(graph.keys())

    prim_start = input("Start node for Prim: ")
    astar_start = input("Start node for A*: ")
    astar_goal = input("Goal node for A*: ")
    dijkstra_start = input("Start node for Dijkstra: ")
    dijkstra_goal = input("Goal node for Dijkstra: ")
    gbfs_start = input("Start node for GBFS: ")
    gbfs_goal = input("Goal node for GBFS: ")

    # Prim
    start = time.time()
    prim_result = prim.prim(graph, prim_start)
    prim_time = time.time() - start

    # Kruskal
    start = time.time()
    nodes = list(graph.keys())
    kruskal_result = kruskal(nodes, edges)
    kruskal_time = time.time() - start

    # A*
    start = time.time()
    path_astar, cost_astar = astar(graph, astar_start, astar_goal, positions)
    astar_time = time.time() - start

    # Dijkstra
    start = time.time()
    path_dijkstra, cost_dijkstra = dijkstra(graph, dijkstra_start, dijkstra_goal)
    dijkstra_time = time.time() - start

    # GBFS
    start = time.time()
    path_gbfs = gbfs(graph, gbfs_start, gbfs_goal, positions)
    gbfs_time = time.time() - start

    # Output
    print("\n--- Result for Weighted Graph ---")
    print(f"Prim MST from {prim_start}: {prim_result} (time: {prim_time:.6f}s)")
    print(f"Kruskal MST: {kruskal_result} (time: {kruskal_time:.6f}s)")
    print(f"A* Path {astar_start} -> {astar_goal}: {path_astar} (cost: {cost_astar}, time: {astar_time:.6f}s)")
    print(f"Dijkstra Path {dijkstra_start} -> {dijkstra_goal}: {path_dijkstra} (cost: {cost_dijkstra}, time: {dijkstra_time:.6f}s)")
    print(f"GBFS Path {gbfs_start} -> {gbfs_goal}: {path_gbfs} (time: {gbfs_time:.6f}s)")

def run_dag():
    print("\n=== Input Directed Acyclic Graph (DAG) ===")
    graph = input_unweighted_graph()

    start = time.time()
    try:
        topo_order = topological_sort(graph)
        elapsed = time.time() - start
        print(f"\n--- Topological Sort Result ---")
        print(f"Topological Order: {topo_order} (time: {elapsed:.6f}s)")
    except ValueError as e:
        elapsed = time.time() - start
        print(f"\nTopological Sort failed: {e} (time: {elapsed:.6f}s)")

def main():
    print("=== Graph Algorithm Comparison ===")
    print("1. Unweighted Graph (BFS, DFS)")
    print("2. Weighted Graph (Prim, Kruskal, A*, Dijkstra, GBFS)")
    print("3. DAG (Topological Sort Only)")
    choice = input("Choose graph type [1/2/3]: ")

    if choice == '1':
        run_unweighted()
    elif choice == '2':
        run_weighted()
    elif choice == '3':
        run_dag()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()




'''
=== Input Unweighted Graph for BFS DFS ===
=== Input Unweighted Graph ===
Number of nodes (unweighted graph): 5
Node name: A
Neighbors of A (comma-separated): B, C
Node name: B
Neighbors of B (comma-separated): A, D
Node name: C
Neighbors of C (comma-separated): A, D
Node name: D
Neighbors of D (comma-separated): B, C, E
Node name: E
Neighbors of E (comma-separated): D
Start node for BFS/DFS: A
Goal node for BFS/DFS: E
 

'''
'''
=== Input Unweighted Graph for DAG ===
Number of nodes (unweighted graph): 5
Node name: A
Neighbors of A (comma-separated): B,D
Node name: B
Neighbors of B (comma-separated): C
Node name: C
Neighbors of C (comma-separated):
Node name: D
Neighbors of D (comma-separated): E
Node name: E
Neighbors of E (comma-separated):

'''
''' 


=== Input Weighted Graph for MST (Prim & Kruskal) ===
Number of edges (weighted graph): 5
Edge (format: node1 node2 weight): A B 3
Edge (format: node1 node2 weight): A C 4
Edge (format: node1 node2 weight): B D 2
Edge (format: node1 node2 weight): C D 5
Edge (format: node1 node2 weight): D E 1

Start node for Prim's algorithm: A

===  input for A* ===
Start node for A*: A
Goal node for A*: E
Enter positions for each node (format: x y):
Position of A: 0 0
Position of B: 1 2
Position of C: 2 0
Position of D: 3 2
Position of E: 4 3

'''