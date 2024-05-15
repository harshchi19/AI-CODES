graph = {
   'A': ['B', 'C'],
   'B': ['D', 'E'],
   'C': ['E','F','B'],
   'D': [],
   'E': [],
   'F': []
}

visited = []
queue = []

def bfs(graph, start):
   if start not in visited:
      visited.append(start)
   for neighbor in graph[start]:
      if neighbor not in visited:
         queue.append(neighbor)
   if queue:
      bfs(graph, queue.pop(0))

start_node = 'A'
bfs(graph, start_node)

for node, edges in graph.items():
   if node in visited:
      print(node,'was visited')
   else:
      print(node,'was not visited')
      
print('\nOrder of visitation was: ')
[print(node, end=' ') for node in visited]