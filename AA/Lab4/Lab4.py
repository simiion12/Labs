from Algorithms import Algorithms
import time
import matplotlib.pyplot as plt
import pandas as pd

# Create a list of graph sizes
values = [4, 8, 16, 32, 64, 128, 256, 512]

# Initialize lists to store execution times
timeDijkstraSparse = []
timeDijkstraDense = []
timeFloydWarshallSparse = []
timeFloydWarshallDense = []

# Generate graphs and measure execution times
for i in values:
    # Generate sparse graph for Dijkstra
    graph = Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraSparse.append(end - start)

    # Generate dense graph for Dijkstra
    graph = Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraDense.append(end - start)

    # Generate sparse graph for Floyd-Warshall
    graph = Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallSparse.append(end - start)

    # Generate dense graph for Floyd-Warshall
    graph = Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallDense.append(end - start)

# Plotting Dijkstra algorithm results
plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Dijkstra Algorithm')
plt.legend()  # Adding legend
plt.show()

# Plotting Floyd-Warshall algorithm results
plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Floyd-Warshall Algorithm')
plt.legend()  # Adding legend
plt.show()

# Plotting both algorithms together
plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Shortest Path Algorithms')
plt.legend()  # Adding legend
plt.show()

# Displaying results in a table
data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timeDijkstraSparse[i], timeDijkstraDense[i], timeFloydWarshallSparse[i], timeFloydWarshallDense[i]])

headers = ["Input Size", 'Dijkstra Sparse', 'Dijkstra Dense', 'Floyd-Warshall Sparse', 'Floyd-Warshall Dense']
df = pd.DataFrame(data, columns=headers)
print(df)
