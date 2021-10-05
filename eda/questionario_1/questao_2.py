import random

def alg1(A, n):
    max_soma = 0
    soma = 0
    num_k = 0
    num_i = 0
    num_j = 0
    for i in range(0, n):
        num_i = num_i + 1
        for j in range(i, n):
            num_j = num_j + 1
            soma = 0
            for k in range(i, j):
                soma = soma + A[k]
                num_k = num_k + 1
            if soma > max_soma:
                max_soma = soma
    return max_soma, num_k, num_i, num_j


for n in range(0,11):
    res = [random.randint(-10,n) for i in range(n)]
    max_soma, num_op, num_i, num_j = alg1(res, n)
    print(f"n={n}, max_soma: {max_soma}, num_ops={num_op}, res={res}, num_i={num_i}, num_j={num_j}")