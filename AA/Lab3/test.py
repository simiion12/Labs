from Algorithms import Graph
from matplotlib import pyplot as plt
import random
import time
import graphviz

graphs = []
vertices_number = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900]
graph_vertices = []
# Creating graphs
for i in range(10):
    g = Graph()  # Create a new Graph instance
    num_vertices = vertices_number[i]
    graph_vertices.append(num_vertices)
    # To ensure there are as many vertices as edges, we create a pair of edges for each vertex
    for j in range(num_vertices):
        # Add edges with random connections ensuring we do not exceed the vertices count
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        g.addEdge(u, v)

    graphs.append(g)

# Plotting with graphviz
for i, g in enumerate(graphs):
    dot = graphviz.Digraph(comment='The Round Table')
    for node in g.graph:
        for neighbor in g.graph[node]:
            dot.edge(str(node), str(neighbor))
    dot.render('graph' + str(i))

timeDFS = []
timeBFS = []
# Iterating over each graph and measuring DFS execution time
for graph in graphs:
    start = time.perf_counter()
    graph.DFS(1)
    end = time.perf_counter()
    timeDFS.append(end - start)

    start = time.perf_counter()
    graph.bfs(1)
    end = time.perf_counter()
    timeBFS.append(end - start)


# Plotting the graph
plt.plot(graph_vertices, timeDFS, label="DFS")
plt.plot(graph_vertices, timeBFS, label="BFS")
plt.xlabel('Graph Vertices')
plt.ylabel('Time taken for DFS')
plt.title('Graph Number vs Time taken for DFS')
plt.legend()
plt.show()
