import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

# Додамо вершини (станції)
G.add_nodes_from([
    (1, {"name": "Станція 1"}),
    (2, {"name": "Станція 2"}),
    (3, {"name": "Станція 3"}),
    (4, {"name": "Станція 4"}),
    (5, {"name": "Станція 5"})
])

# Додамо ребра
G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 1),
    (1, 3),
    (2, 4)
])

labels = nx.get_node_attributes(G, 'name')


# Візуалізація графу
def graph_vizualization(title: str):
    pos = nx.spring_layout(G)  # Розташування вершин
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

    plt.title(title)
    plt.show()


# Виведемо граф
graph_vizualization(title="Транспортна мережа міста")

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for node, degree in degrees.items():
    print(f"Вершина {node} ({labels[node]}): {degree}")
