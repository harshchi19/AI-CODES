import random

# Define the problem parameters
num_cities = 4
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Define the ACO parameters
num_ants = 10
max_iterations = 100
alpha = 1
beta = 2
rho = 0.5
Q = 1

# Initialize the pheromone matrix
pheromones = [[1 / (num_cities * num_cities) for _ in range(num_cities)] for _ in range(num_cities)]

# ACO algorithm
best_cost = float('inf')
best_solution = []

for iteration in range(max_iterations):
    solutions = []
    
    #make a set of solutions with their corresponding costs
    for ant in range(num_ants):
        solution = []
        start_city = random.randint(0, num_cities - 1)
        unvisited = set(range(num_cities))
        unvisited.remove(start_city)
        solution.append(start_city)

        current_city = start_city
        while unvisited:
            next_city = max(unvisited, 
    key=lambda city: (pheromones[current_city][city] ** alpha) / ( distances[current_city][city]) ** beta)
    
            solution.append(next_city)
            unvisited.remove(next_city)
            current_city = next_city

        solutions.append((solution, sum(distances[solution[i]][solution[(i + 1) % len(solution)]] for i in range(len(solution)))))

    #get the best solution with cost
    solutions.sort(key=lambda x: x[1])
    best_solution_iteration, best_cost_iteration = solutions[0]

    #update overall best if a better one found
    if best_cost_iteration < best_cost:
        best_cost, best_solution = best_cost_iteration, best_solution_iteration

    #Evaporate the pheromone trails 
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= (1 - rho)

    #Increase pheromone on better trails
    for solution, cost in solutions:
        for i in range(len(solution)):
            city_a, city_b = solution[i], solution[(i + 1) % len(solution)]
            pheromones[city_a][city_b] += Q / cost

# Print the best solution and its cost
print(f"Best solution: {best_solution}")
print(f"Best cost: {best_cost}")