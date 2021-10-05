import random
import time

def max_num_list(input):
    max = 0
    for i in input:
        if i > max:
            max = i
    return max


def algoritmo1(input, num_elements):
    local_input = input.copy()
    res = list()

    tic = time.perf_counter()
    for i in range(0, num_elements):
        max = max_num_list(local_input)
        res.append(max)
        local_input.remove(max)
    
    toc = time.perf_counter()

    print(f"Algoritmo1 O(n): Numero elementos mais caros={num_elements}. Tempo {toc - tic:0.4f} seconds")

    return res


def algoritmo2(input, num_elements):
    local_input = input.copy()

    tic = time.perf_counter()
    local_input.sort()
    res = local_input[len(local_input)-num_elements:]
    
    toc = time.perf_counter()

    print(f"Algoritmo2 O(n log n): Numero elementos mais caros={num_elements}. Tempo {toc - tic:0.4f} seconds")

    return res

limit = 10**7
input = [random.randint(0, limit) for i in range(limit)]

algoritmo1(input, num_elements=10)
algoritmo1(input, num_elements=100)
algoritmo1(input, num_elements=1000)

algoritmo2(input, num_elements=10)
algoritmo2(input, num_elements=100)
algoritmo2(input, num_elements=1000)






