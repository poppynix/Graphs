
from queue import PriorityQueue

def prim_mst(graph, start):
    visited = set()
    pq = PriorityQueue()
    mst = []

    visited.add(start)
    for neighbor, weight in graph[start]:
        pq.put((weight, start, neighbor))

    while not pq.empty() and len(visited) < len(graph):
        weight, frm, to = pq.get()
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for neighbor, edge_weight in graph[to]:
                if neighbor not in visited:
                    pq.put((edge_weight, to, neighbor))

    return mst

#graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

#calling the function from the first node A
mst = prim_mst(graph, 'A')

#output 
print("Minimum Spanning Tree edges:")
for edge in mst:
    print(edge)
