import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()
edge_labels = dict()

# Create the graph using a CSV file.
# Lines of length 1 are nodes.
# Any following lines of length 2 or more are edges of the form:
#   neighbor, label, label...
with open("project.csv", "r") as file:
    node = None
    for line in file:
        if not line.strip():  # skip blank lines
            continue
        line = [s.strip() for s in line.split(',')]  # separate all the strings in the line
        if len(line) == 1:
            node = line[0]
            G.add_node(node)
        elif len(line) > 1:
            # neighbor, labels = line[0], line[1:]
            neighbor, label = line[0], line[1]
            edge = (node, neighbor)
            G.add_edge(*edge, label=label)
            edge_labels[edge] = label



# pos = nx.spring_layout(G)
# pos = nx.kamada_kawai_layout(G)
pos = nx.planar_layout(G)
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_color='red'
)


def most_referenced_node() -> str:
    return sorted(G.in_degree, key=lambda x: x[1])[-1][0]

def get_references(node) -> list:
    return [v for u, v in G.out_edges(node)]

def get_referenced_by(node) -> list:
    return [u for u, v in G.in_edges(node)]


print(f"The most referenced node is: {most_referenced_node()}")
#print(shortest_path(source, target)) #to be used to calculate the distance(relation between two genes, once weights have been added to the edges)
plt.show()
