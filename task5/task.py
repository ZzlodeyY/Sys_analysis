import json
import numpy as np

def get_rankings(structure):
    return {elem: idx for idx, item in enumerate(structure) for elem in (item if isinstance(item, list) else [item])}

def build_matrix(rankings):
    size = len(rankings)
    return [
        [1 if rankings[key] >= rankings[i] else 0 for key in rankings]
        for i in range(1, size + 1)
    ]

def compute_kernel(mat_a, mat_b):
    mat_a, mat_b = np.array(mat_a), np.array(mat_b)
    return np.logical_or(mat_a * mat_b, mat_a.T * mat_b.T)

def main(data_a, data_b):
    rankings_a, rankings_b = get_rankings(data_a), get_rankings(data_b)
    matrix_a, matrix_b = build_matrix(rankings_a), build_matrix(rankings_b)
    kernel = compute_kernel(matrix_a, matrix_b)
    print(kernel)

if __name__ == "__main__":
    input_a = [1, [2, 3], 4, [5, 6, 7], 8, 9, 10]
    input_b = [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]
    main(input_a, input_b)
