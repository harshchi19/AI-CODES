import random

# Define the function to optimize
def fitness_function(x):
  return x**2

# Define parameters
population_size = 10
chromosome_length = 10
mutation_rate = 0.1
generations = 100

# Generate initial population
population = []
for _ in range(population_size):
  chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
  population.append(chromosome)

# Main loop for generations
for generation in range(generations):
  # Calculate fitness for each chromosome
  fitness_scores = []
  for chromosome in population:
    x = int("".join(map(str, chromosome)), 2)  # Convert chromosome to integer
    fitness = fitness_function(x)
    fitness_scores.append(fitness)

  # Select parents based on fitness
  parents = []
  for _ in range(population_size):
    # Use roulette wheel selection
    total_fitness = sum(fitness_scores)
    selection_point = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for i, score in enumerate(fitness_scores):
      cumulative_fitness += score
      if cumulative_fitness >= selection_point:
        parents.append(population[i])
        break

  # Crossover and mutation
  new_population = []
  for i in range(0, population_size, 2):
    parent1, parent2 = parents[i], parents[i+1]
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    # Apply mutation
    for j in range(chromosome_length):
      if random.random() < mutation_rate:
        child1[j] ^= 1  # Flip the bit
      if random.random() < mutation_rate:
        child2[j] ^= 1
    
    new_population.append(child1)
    new_population.append(child2)

  population = new_population

# Find the best chromosome in the final population
best_chromosome = population[0]
best_fitness = fitness_scores[0]
for i in range(1, population_size):
  if fitness_scores[i] > best_fitness:
    best_chromosome = population[i]
    best_fitness = fitness_scores[i]

# Print the results
best_x = int("".join(map(str, best_chromosome)), 2)
print("Best chromosome:", best_chromosome)
print("Best x:", best_x)
print("Best fitness:", best_fitness)
