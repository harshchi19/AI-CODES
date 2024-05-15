from aco_routing import ACO
import networkx as nx

G = nx.DiGraph()

G.add_edge("A", "B", cost=2)
G.add_edge("B", "C", cost=2)
G.add_edge("A", "H", cost=2)
G.add_edge("H", "G", cost=2)
G.add_edge("C", "F", cost=1)
G.add_edge("F", "G", cost=1)
G.add_edge("G", "F", cost=1)
G.add_edge("F", "C", cost=1)
G.add_edge("C", "D", cost=10)
G.add_edge("E", "D", cost=2)
G.add_edge("G", "E", cost=2)

aco = ACO(G, ant_max_steps=100, num_iterations=100, ant_random_spawn=True)

aco_path, aco_cost = aco.find_shortest_path(source="A", destination="D", num_ants=100)

print("ACO Path: ", end="")
for i, node in enumerate(aco_path):
    if i != 0:
        print(" -> ", end="")
    print(node, end="")

print("\nACO Cost:", aco_cost)