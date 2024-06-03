import networkx as nx
import matplotlib.pyplot as plt
from task_1 import (G,
                    labels)

 # Додамо ребра з вагами
G.add_weighted_edges_from([
    (1, 2, 1.5),
    (2, 3, 2.0),
    (3, 4, 2.5),
    (4, 5, 1.0),
    (5, 1, 2.2),
    (1, 3, 2.8),
    (2, 4, 1.7)
])


# Пошук найкоротшого шляху
def find_all_shortest_paths(G):
    all_shortest_paths = {}
    for source in G.nodes:
        shortest_paths = nx.single_source_dijkstra_path(G, source)
        all_shortest_paths[source] = shortest_paths
    return all_shortest_paths


# Знаходження найкоротших шляхів між усіма вершинами
all_shortest_paths = find_all_shortest_paths(G)

# Візуалізація графу з вагами ребер
pos = nx.spring_layout(G)  # Розташування вершин
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G,
        pos,
        with_labels=True,
        labels=labels,
        node_size=700,
        node_color="skyblue",
        font_size=10,
        font_color="black",
        font_weight="bold",
        edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Транспортна мережа міста з вагами")
plt.show()

# Виведення найкоротших шляхів
for source, paths in all_shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {source} ({labels[source]}):")
    for target, path in paths.items():
        print(f"  до вершини {target} ({labels[target]}): шлях {path} з довжиною {nx.dijkstra_path_length(G, source, target)}")