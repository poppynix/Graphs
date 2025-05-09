from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  # adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        in_degree = [0] * self.V

        # Step 1: Compute in-degree of each vertex
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Step 2: Enqueue vertices with in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])
        top_order = []

        count = 0

        # Step 3: Process the queue
        while queue:
            u = queue.popleft()
            top_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

            count += 1

        # Step 4: Check for cycle
        if count != self.V:
            print("Cycle detected, topological sort not possible.")
        else:
            print("Topological Order:", top_order)

# Example usage
g = Graph(8)
g.add_edge(7, 6)
g.add_edge(7, 5)
g.add_edge(5, 4)
g.add_edge(6, 4)
g.add_edge(6, 3)
g.add_edge(5, 2)
g.add_edge(3, 1)
g.add_edge(2, 1)
g.add_edge(1, 0)
g.topological_sort()
