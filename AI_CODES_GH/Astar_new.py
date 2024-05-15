graph = {}

def add_edge(node1, node2, weight):
    if node1 not in graph:
        graph[node1] = []
    graph[node1].append((node2, weight))

def get_neighbours(node):
    return graph[node]

def AStar(start, goal):
    open_list = [(0, start, [])]
    closed_list = set()
    while open_list:
        val, node, path = min(open_list)
        open_list.remove((val, node, path))
        if node == goal:
            print(f"The best path is: {path + [node]}")
            return val
        elif node not in closed_list:
            closed_list.add(node)
            for neighbour, cost in get_neighbours(node):
                if neighbour not in closed_list:
                    total = val + cost
                    open_list.append((total, neighbour, path + [node]))

# Take input from the user to define the graph
num_edges = int(input("Enter the number of edges: "))
print("Enter edges in the format 'node1 node2 weight':")
for _ in range(num_edges):
    edge_input = input().split()
    add_edge(edge_input[0], edge_input[1], int(edge_input[2]))

# Specify the start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Run A* algorithm
optimal_path_cost = AStar(start_node, goal_node)
print("Optimal Path Cost:", optimal_path_cost)
