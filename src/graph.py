import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def create_graph(edges, nodes_amount, nodes_with_reach=None):

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph
    
    # Add nodes to the graph with a 'reach_set' attribute that represents the nodes within scope
    if nodes_with_reach is None:
        G.add_nodes_from(range(1, nodes_amount + 1))
    else:
        for node, reach_set in nodes_with_reach.items():
            G.add_node(node, reach_set=reach_set)

    # Add edges to the graph
    for u, v, weight in edges:
        link_quality = np.random.uniform(0.5, 1.0)  # Random link quality between 0.5 and 1.0
        G.add_edge(u, v, weight=weight, link_quality=link_quality)
        if nodes_with_reach: G.add_edge(v, u, weight=weight, link_quality=link_quality)  # Add reverse directio

    # Return graph
    return G

# Function to display the graph in DODAG form
def draw_dodag(graph, root):
    pos = {}
    layer = 0
    current_layer_nodes = [root]
    next_layer_nodes = []
    while current_layer_nodes:
        for i, node in enumerate(current_layer_nodes):
            pos[node] = (i, -layer)  # Align nodes on current layer
            next_layer_nodes.extend(graph.successors(node))  # Add child nodes to the next layer
        current_layer_nodes = next_layer_nodes
        next_layer_nodes = []
        layer += 1
    
    labels = {edge: f"{graph.edges[edge]['weight']}/{graph.edges[edge]['link_quality']:.2f}" for edge in graph.edges}

    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("DODAG with link quality")
    plt.show()