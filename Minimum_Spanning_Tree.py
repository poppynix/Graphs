
import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = []
    mst = []

    # Add all edges from the start node
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    while min_heap and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for neighbor, edge_weight in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, to, neighbor))

    return mst

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst = prim_mst(graph, 'A')
print("Minimum Spanning Tree edges:")
for edge in mst:
    print(edge)


