import random 

def fitness_function(chromosome):
   x = int("".join(map(str, chromosome)), 2)
   return x ** 2

popultaion_size = 10
chromosome_length = 10
genereations = 200
mutation_rate = 0.1 #%

population = []
for _ in range(popultaion_size):
   chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
   population.append(chromosome)

for _ in range(genereations):
    fitness_scores = []
    for chromosome in population:
       fitness = fitness_function(chromosome)
       fitness_scores.append(fitness)

    parents = []
    for _ in range(popultaion_size):
        parents.append(random.choice(population))

    children = []
    for i in range(0, len(parents), 2):
        crossover_point = random.randint(0, chromosome_length-1)
        parent1 = parents[i]
        parent2 = parents[i+1]

        child1 = parent1[:crossover_point] + parent2[crossover_point:] 
        child2 = parent2[:crossover_point] + parent1[crossover_point:] 
    
        for j in range(chromosome_length):
            if random.random() < mutation_rate:
                child1[j] ^= 1
            if random.random() < mutation_rate:
                child2[j] ^= 1

        children.append(child1)
        children.append(child2)

    population = children

best_chromosome = max(population, key = lambda a : fitness_function(a))
best_fitness = fitness_function(best_chromosome)

best_x = best_fitness ** 0.5

print(best_chromosome, best_fitness, best_x)    