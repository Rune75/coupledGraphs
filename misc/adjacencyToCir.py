import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency list
adj_list = {
    'R1': ['C1', 'V1'],
    'C1': ['R1', 'V1'],
    'V1': ['R1', 'C1']
}

# Create a graph from the adjacency list
G = nx.Graph(adj_list)

# Draw the graph
pos = nx.spring_layout(G)  # layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

# Display the plot
plt.show()
