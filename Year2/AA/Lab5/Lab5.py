from Algorithms import Algorithms
import time

sizes = [10, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]
prim_times = []
kruskal_times = []

for size in sizes:
    graph = Algorithms.generate_random_graph(size)
    start = time.time()
    Algorithms.prim(graph)
    prim_times.append(time.time() - start)

    start = time.time()
    Algorithms.kruskal(graph)
    kruskal_times.append(time.time() - start)


# Plotting the result
import matplotlib.pyplot as plt

plt.plot(sizes, prim_times, label="Prim's Algorithm")
plt.plot(sizes, kruskal_times, label="Kruskal's Algorithm")
plt.xlabel("Number of Nodes")
plt.ylabel("Runtime (seconds)")
plt.title("Empirical Analysis of Prim's and Kruskal's Algorithms")
plt.legend()
plt.show()
