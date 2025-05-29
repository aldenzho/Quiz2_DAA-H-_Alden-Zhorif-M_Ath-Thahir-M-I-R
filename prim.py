import heapq

def prim(graph, start):
    visited = set()
    mst = []
    heap = [(0, start, None)]
    
    while heap:
        cost, u, parent = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            if parent:
                mst.append((parent, u, cost))
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (w, v, u))
    return mst
'''

===========OPSI TAMBAHN FITUR===============

import matplotlib.pyplot as plt
def visualize_mst(mst, positions):
    plt.figure(figsize=(8, 6))
    
    # Gambar edges MST
    for u, v, w in mst:
        x_values = [positions[u][0], positions[v][0]]
        y_values = [positions[u][1], positions[v][1]]
        plt.plot(x_values, y_values, 'b-', linewidth=2)
        
        # Tulis bobot di tengah edge
        mid_x = (positions[u][0] + positions[v][0]) / 2
        mid_y = (positions[u][1] + positions[v][1]) / 2
        plt.text(mid_x, mid_y, str(w), color='red', fontsize=10)

    # Gambar node sebagai titik dan label
    for node, (x, y) in positions.items():
        plt.plot(x, y, 'ko')
        plt.text(x, y, f" {node}", verticalalignment='bottom', fontsize=12)
    
    plt.title("Minimum Spanning Tree Visualization (Prim's MST)")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def input_positions_and_visualize(nodes, mst):
    print("\nEnter positions for each node for visualization (format: x y):")
    positions = {}
    for node in nodes:
        x, y = map(float, input(f"Position of {node}: ").split())
        positions[node] = (x, y)

    visualize_mst(mst, positions)
    return positions
'''

