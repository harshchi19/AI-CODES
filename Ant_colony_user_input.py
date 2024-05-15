import numpy as np
import itertools as it

def input_matrix():
    n = int(input("Enter the number of cities:"))
    d = np.zeros((n, n))
    print("Enter the distance of each pair")
    for i in range(n):
        for j in range(n):
            d[i,j] = int(input(f"Enter the distance of city {i+1} to city {j+1}:"))
    return d

def generate_tours(n):
    return list(it.permutations(range(n)))

def print_all_tours(d):
    n = len(d)
    tours = generate_tours(n)
    for t in tours:
        l = total_distance(t, d)
        print('Tour:', t, ' Tour Length:', l)

def ant_colony(d, s, n_a=10, n_i=100, evap=0.5, alpha=1, beta=2):
    n = len(d)
    p = np.ones((n, n)) / n
    best_tour = None
    best_dist = float('inf')
    for i in range(n_i):
        ant_tour = []
        for a in range(n_a):
            c = s
            v = [c]
            u = list(range(n))
            u.remove(c)
            while u:
                prob = [(p[c, nc]**alpha)*(1/d[c, nc]**beta) for nc in u]
                prob /= np.sum(prob)
                nc = np.random.choice(u, p=prob)
                v.append(nc)
                u.remove(nc)
                c = nc
            ant_tour.append(v)
        for t in ant_tour:
            l = total_distance(t, d)
            if l < best_dist:
                best_dist = l
                best_tour = t
        p *= (1-evap)
        for t in ant_tour:
            for i in range(n):
                p[t[i % n], t[(i + 1) % n]] += 1.0 / total_distance(t, d)
    return best_tour, best_dist

def total_distance(t, d):
    total = 0
    n = len(t)
    for i in range(n):
        total += d[t[i % n], t[(i + 1) % n]]
    return total

def main():
    d = input_matrix()
    s = int(input("Enter the start node:"))
    print_all_tours(d)
    best_tour, best_dist = ant_colony(d, s)
    print("Best tour:", best_tour + [s])
    print("Length of best tour:", best_dist)

if __name__ == "__main__":
    main()
