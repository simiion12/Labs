# Prim and Kruskal algorithms for minimum spanning tree
import heapq
import random

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Algorithms:
    def prim(graph):
        min_span_tree = []
        visited = set()
        start_node = next(iter(graph))
        visited.add(start_node)
        edges = [(cost, start_node, node) for node, cost in graph[start_node]]
        heapq.heapify(edges)

        while edges:
            cost, src, dest = heapq.heappop(edges)
            if dest not in visited:
                visited.add(dest)
                min_span_tree.append((src, dest, cost))
                for node, cost in graph[dest]:
                    if node not in visited:
                        heapq.heappush(edges, (cost, dest, node))

        return min_span_tree

    def kruskal(graph):
        min_span_tree = []
        edges = [(cost, src, dest) for src in graph for dest, cost in graph[src]]
        edges.sort()
        disjoint_set = DisjointSet(len(graph))

        for cost, src, dest in edges:
            if disjoint_set.find(src) != disjoint_set.find(dest):
                min_span_tree.append((src, dest, cost))
                disjoint_set.union(src, dest)

        return min_span_tree

    def generate_random_graph(n, max_weight=100):
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
                graph[j].append((i, weight))
        return graph