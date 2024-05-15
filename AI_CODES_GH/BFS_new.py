def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))  # Use get() to handle missing keys

    return visited

graph = {}

# Get graph input from user
while True:
    node = input("Enter a node (or type 'done' to finish): ")
    if node.lower() == 'done':
        break
    neighbors_input = input(f"Enter neighbors for node {node} separated by commas: ")
    neighbors = neighbors_input.split(',') if neighbors_input else []
    graph[node] = [neighbor.strip() for neighbor in neighbors]

start_node = input("Enter the starting node: ")

visited_nodes = bfs(graph, start_node)

print("\nVisited nodes:")
for node in graph:
    if node in visited_nodes:
        print(f"{node} was visited")
    else:
        print(f"{node} was not visited")

print("\nOrder of visitation:")
print(' '.join(visited_nodes))
