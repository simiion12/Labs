# Implementation of dijkstra and floyd warshall algorithm
import heapq
import random
class Algorithms:
    # Dijkstra which will return distance
    def dijkstra(graph, start):
        # Create a dictionary to store the distance of each node from the start node
        distance = {node: float('infinity') for node in graph}
        distance[start] = 0

        # Create a priority queue to store the nodes to visit
        nodes_to_visit = [(0, start)]

        while nodes_to_visit:
            # Get the node with the smallest distance
            current_distance, current_node = heapq.heappop(nodes_to_visit)

            # Iterate over the neighbors of the current node
            for neighbor, weight in graph[current_node].items():
                distance_through_current = current_distance + weight

                # If the distance is smaller than the current distance, update the distance
                if distance_through_current < distance[neighbor]:
                    distance[neighbor] = distance_through_current
                    heapq.heappush(nodes_to_visit, (distance_through_current, neighbor))

        return distance

    # Floyd Warshall algorithm which will return the shortest path between all pairs of nodes

    def floyd_warshall(graph):
        # Initialize the distance matrix
        distance = {node: {neighbor: float('infinity') for neighbor in graph} for node in graph}
        for node in graph:
            distance[node][node] = 0
            for neighbor, weight in graph[node].items():
                distance[node][neighbor] = weight

        # Floyd Warshall algorithm
        for k in graph:
            for i in graph:
                for j in graph:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        return distance

    # Generate graph

    def generate_sparse_graph(nodes, edges):
        graph = {i: {} for i in range(nodes)}
        for _ in range(edges):
            node1, node2 = random.sample(range(nodes), 2)
            weight = random.randint(1, 10)
            graph[node1][node2] = weight
            graph[node2][node1] = weight
        return graph

    def generate_dense_graph(nodes):
        graph = {i: {j: random.randint(1, 10) for j in range(nodes) if j != i} for i in range(nodes)}
        return graph




