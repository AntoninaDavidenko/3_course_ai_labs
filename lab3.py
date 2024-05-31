import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x * np.sin(5 * x)


def decode(population, n_bits, bounds):
    min, max = bounds
    decoded_list = []
    D = (max - min) / 2 ** n_bits
    for x in population:
        binary_str = ''.join(map(str, x))
        number = int(binary_str, 2)
        # масштабування числа до потрібного діапазону
        nx = min + number * D
        decoded_list.append(nx)
    return decoded_list


def selection(population, scores, maximum, k=3):
    tournament_indices = np.random.choice(len(population), size=k, replace=False)
    tournament_parents = [population[i] for i in tournament_indices]
    tournament_fitness = [scores[i] for i in tournament_indices]

    if maximum is True:
        best_index = np.argmax(tournament_fitness)
    else:
        best_index = np.argmin(tournament_fitness)

    return tournament_parents[best_index]


def crossover(par1, par2):
    crossover_point = np.random.randint(1, len(par1))

    # Скрещиваем родителей
    child1 = list(par1[:crossover_point]) + list(par2[crossover_point:])
    child2 = list(par2[:crossover_point]) + list(par1[crossover_point:])

    return np.array(child1), np.array(child2)


def mutation(child, mutation_rate):
    mutated_child = np.copy(child)
    for i in range(len(mutated_child)):
        if np.random.rand() < mutation_rate:
            mutated_child[i] = 1 if mutated_child[i] == 0 else 0

    return mutated_child


def genetic(max_generation, max_stagnation, maximum, bounds):
    stagnation = 0
    generation = 0
    population = np.random.randint(2, size=(100, 16))
    decoded = decode(population, 16, bounds)
    fitness = [func(d) for d in decoded]
    if maximum is True:
        best_fitness = np.max(fitness)
    else:
        best_fitness = np.min(fitness)
    index_best_fitness = fitness.index(best_fitness)
    best_chromosome = decoded[index_best_fitness]
    print("Best chromosome: y=", best_fitness, "x=", best_chromosome)

    while generation < max_generation:
        parents = []
        for x in range(len(population)):
            parents.append(selection(population, fitness, maximum))

        children = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, 0.1)
            child2 = mutation(child2, 0.1)
            children.append(child1)
            children.append(child2)

        population = children
        decoded = decode(population, 16, bounds)
        fitness = [func(d) for d in decoded]
        if maximum is True:
            best_fitness_ = np.max(fitness)
        else:
            best_fitness_ = np.min(fitness)
        index_best_fitness_ = fitness.index(best_fitness_)
        if abs(best_fitness_) > abs(best_fitness):
            best_fitness = best_fitness_
            best_chromosome = decoded[index_best_fitness_]
            print("New best found: y=", best_fitness, "x=", best_chromosome, "generation:", generation)
            stagnation = 0
        else:
            stagnation += 1

        if stagnation >= max_stagnation:
            break
        generation += 1
    return best_fitness, best_chromosome, generation


bounds = [-2, 5]


print("Best chromosome for maximization: y= %s x = %s generation: %s" % genetic(1000, 100, True, bounds))
print("Best chromosome for minimization: y= %s x = %s  generation: %s" % genetic(1000, 100, False, bounds))


x = np.linspace(-2, 5, 1000)

plt.plot(x, func(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title('x * np.sin(5 * x)')
plt.show()
