def get_neighbors(adjacency_list, v):
    return adjacency_list[v]

def h(node, heuristic):
    return heuristic[node]

def a_star_algorithm(adjacency_list, heuristic, start_node, stop_node):

    open_list = set([start_node])
    closed_list = set([])

    g = {}
    g[start_node] = 0
    parents = {}
    parents[start_node] = start_node

    while len(open_list) > 0:
        n = None
        for v in open_list:
            if n == None or g[v] + h(v, heuristic) < g[n] + h(n, heuristic):
                n = v

        if n == None:
            print('Path does not exist!')
            return None, None

        if n == stop_node:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_node)
            reconst_path.reverse()

            total_cost = g[stop_node]

            print(f'Path found: {reconst_path}')
            print(f'Total cost: {total_cost}')
            return reconst_path, total_cost

        for (m, weight) in get_neighbors(adjacency_list, n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)
    print('Path does not exist!')
    return None, None

adjacency_list = {}
heuristic = {}

while True:
    node = input("Enter node (or 'done' to finish): ")
    if node.lower() == 'done':
        break
    neighbors = input("Enter neighbors and weights separated by commas (e.g., B,4,C,3): ").split(',')
    adjacency_list[node] = [(neighbors[i], int(neighbors[i+1])) for i in range(0, len(neighbors), 2)]
    heuristic[node] = int(input(f"Enter heuristic for node {node}: "))

start_node = input("Enter start node: ")
stop_node = input("Enter stop node: ")

path, cost = a_star_algorithm(adjacency_list, heuristic, start_node, stop_node)

if path:
    print("Path:", path)
    print("Total Cost:", cost)