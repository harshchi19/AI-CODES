def dfs(graph, start_node, visited):
    if start_node not in visited:
        visited.append(start_node)
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}

# Get graph input from user
while True:
    node = input("Enter a node (or type 'done' to finish): ")
    if node.lower() == 'done':
        break
    neighbors = input(f"Enter neighbors for node {node} separated by commas: ").split(',')
    graph[node] = [neighbor.strip() for neighbor in neighbors]

start_node = input("Enter the starting node: ")
visited_nodes = []

dfs(graph, start_node, visited_nodes)

print("\nVisited nodes:")
for node in graph:
    if node in visited_nodes:
        print(f"{node} was visited")
    else:
        print(f"{node} was not visited")

print("\nOrder of visitation:")
print(' '.join(visited_nodes))
