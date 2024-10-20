import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency list for 4 sub-circuits with a shared 5-pin edge connector (common backplane)
adj_list = {
    # Sub-circuit 1
    'S1': ['P1', 'J1', 'N1', 'G1', 'E1'],
    'P1': ['S1', 'N1'],
    'J1': ['S1', 'G1'],
    'N1': ['S1', 'P1'],
    'G1': ['S1', 'J1'],

    # Sub-circuit 2
    'S2': ['P2', 'J2', 'N2', 'G2', 'E2'],
    'P2': ['S2', 'N2'],
    'J2': ['S2', 'G2'],
    'N2': ['S2', 'P2'],
    'G2': ['S2', 'J2'],

    # Sub-circuit 3
    'S3': ['P3', 'J3', 'N3', 'G3', 'E3'],
    'P3': ['S3', 'N3'],
    'J3': ['S3', 'G3'],
    'N3': ['S3', 'P3'],
    'G3': ['S3', 'J3'],

    # Sub-circuit 4
    'S4': ['P4', 'J4', 'N4', 'G4', 'E4'],
    'P4': ['S4', 'N4'],
    'J4': ['S4', 'G4'],
    'N4': ['S4', 'P4'],
    'G4': ['S4', 'J4'],

    # Common edge connector (shared backplane)
    'E1': ['S1', 'S2', 'S3', 'S4'],  # Pin 1 connected to all sub-circuits
    'E2': ['P1', 'P2', 'P3', 'P4'],  # Pin 2 connected to all sub-circuits
    'E3': ['J1', 'J2', 'J3', 'J4'],  # Pin 3 connected to all sub-circuits
    'E4': ['N1', 'N2', 'N3', 'N4'],  # Pin 4 connected to all sub-circuits
    'E5': ['G1', 'G2', 'G3', 'G4']   # Pin 5 connected to all sub-circuits
}

# Create the graph from the updated adjacency list
G = nx.Graph(adj_list)

# Define fixed positions for the nodes in 4 blocks (sub-circuits) and shared edge connectors
pos = {
    # Sub-circuit 1 (top-left block)
    'S1': (0, 4), 'P1': (1, 4), 'J1': (0, 3), 'N1': (1, 3), 'G1': (0.5, 2.5),

    # Sub-circuit 2 (top-right block)
    'S2': (3, 4), 'P2': (4, 4), 'J2': (3, 3), 'N2': (4, 3), 'G2': (3.5, 2.5),

    # Sub-circuit 3 (bottom-left block)
    'S3': (0, 1), 'P3': (1, 1), 'J3': (0, 0), 'N3': (1, 0), 'G3': (0.5, -0.5),

    # Sub-circuit 4 (bottom-right block)
    'S4': (3, 1), 'P4': (4, 1), 'J4': (3, 0), 'N4': (4, 0), 'G4': (3.5, -0.5),

    # Shared edge connector (common backplane) positioned in the middle
    'E1': (2, 4.5), 'E2': (2, 3.5), 'E3': (2, 2.5), 'E4': (2, 1.5), 'E5': (2, 0.5)
}

# Compute the shortest path between two nodes (e.g., from S1 to G4)
shortest_path = nx.shortest_path(G, source='S1', target='G4')

# Draw the entire graph with constant node positions
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)

# Highlight the shortest path in red
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# Add block labels or rectangular areas to represent sub-circuits
# Draw a box around Sub-circuit 1
plt.gca().add_patch(plt.Rectangle((-0.5, 2.5), 2, 2, edgecolor='blue', facecolor='none', lw=2))
plt.text(0.25, 4.5, 'Sub-circuit 1', fontsize=12, color='blue')

# Draw a box around Sub-circuit 2
plt.gca().add_patch(plt.Rectangle((2.5, 2.5), 2, 2, edgecolor='green', facecolor='none', lw=2))
plt.text(3.75, 4.5, 'Sub-circuit 2', fontsize=12, color='green')

# Draw a box around Sub-circuit 3
plt.gca().add_patch(plt.Rectangle((-0.5, -0.5), 2, 2, edgecolor='purple', facecolor='none', lw=2))
plt.text(0.25, 1.5, 'Sub-circuit 3', fontsize=12, color='purple')

# Draw a box around Sub-circuit 4
plt.gca().add_patch(plt.Rectangle((2.5, -0.5), 2, 2, edgecolor='orange', facecolor='none', lw=2))
plt.text(3.75, 1.5, 'Sub-circuit 4', fontsize=12, color='orange')

# Display the schematic with the highlighted shortest path
plt.title("Schematic with Common Backplane (5-pin Shared Connector) and Highlighted Shortest Path")
plt.axis('off')
plt.show()
