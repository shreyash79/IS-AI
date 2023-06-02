import heapq

def prim(graph):
    start_node = list(graph.keys())[0]  # Start with an arbitrary node
    visited = set([start_node])
    min_heap = []
    minimum_spanning_tree = []

    # Initialize with the edges from the start node
    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            minimum_spanning_tree.append((u, v, weight))

            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return minimum_spanning_tree

# Example usage
# Define your graph as an adjacency list

# Sample graph representation (undirected graph)
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 3)],
    'C': [('A', 1), ('B', 2), ('D', 6)],
    'D': [('B', 3), ('C', 6)]
}

minimum_spanning_tree = prim(graph)

# Output the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
