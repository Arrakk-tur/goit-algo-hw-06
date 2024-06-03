import networkx as nx
import matplotlib.pyplot as plt
from task_1 import (G,
                    graph_vizualization,
                    labels)

# import task_1

# Граф з задачі 1
# G = task_1.G

# Визначимо вершини для пошуку шляху
start_node = 1
end_node = 4

# DFS
dfs_path = list(nx.dfs_edges(G, source=start_node))
dfs_path_nodes = nx.dfs_tree(G, source=start_node).nodes
print("Шлях за допомогою DFS:")
print(dfs_path_nodes)

# BFS
bfs_path = list(nx.bfs_edges(G, source=start_node))
bfs_path_nodes = nx.bfs_tree(G, source=start_node).nodes
print("Шлях за допомогою BFS:")
print(bfs_path_nodes)

# Візуалізація шляхів DFS та BFS
pos = nx.spring_layout(G)

plt.figure(figsize=(14, 7))

# Оригінальний граф
# labels = task_1.labels
graph_vizualization(title="Оригінальний граф")

# Граф з виділеними шляхами
plt.subplot(122)
nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=10, font_color="black",
        font_weight="bold", edge_color="gray")
nx.draw_networkx_edges(G, pos, edgelist=dfs_path, edge_color="r", width=2)
nx.draw_networkx_edges(G, pos, edgelist=bfs_path, edge_color="b", width=2)
plt.title("Шляхи DFS (червоний) та BFS (синій)")

plt.show()
