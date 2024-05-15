def get_neighbours(v):
   return adjacency_list[v]

def aStar( start_node, end_node):
    open_list = { start_node }
    g = { start_node: 0}
    parent = { start_node: start_node }

    while open_list:
        n = min(open_list, key= lambda a : g[a] + h[a])

        if n == None:
            print('Path not Found!')
            return
        
        if n == end_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print('Path is ', path)
            return path
        
        open_list.remove(n)
        for m, weight in get_neighbours(n):
            temp = g.get(n, 9999) + weight
            if temp < g.get(m, 9999):
                parent[m] = n
                g[m] = temp
                open_list.add(m)

    print('Path not Found!')
    return
                
adjacency_list = {
   'A': [('B', 4), ('C', 3)],
   'B': [('F', 5)],
   'C': [('D', 7), ('E', 10)],
   'D': [('E', 3)],
   'F': [('E', 3)]
}
h = { 'A': 1,
      'B': 1,
      'C': 1,
      'D': 1,
      'E': 1,
      'F': 1
   }
aStar('A', 'E')