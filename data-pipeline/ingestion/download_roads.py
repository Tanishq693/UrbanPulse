import osmnx as ox
import os

place = "Colaba, Mumbai, Maharashtra, India"

G = ox.graph_from_place(
    place,
    network_type="drive"
)

nodes, edges = ox.graph_to_gdfs(G)

os.makedirs("data", exist_ok=True)

nodes.to_parquet("data/nodes.parquet")
edges.to_parquet("data/roads.parquet")

print("Nodes:", len(nodes))
print("Road segments:", len(edges))

ox.plot_graph(G)
