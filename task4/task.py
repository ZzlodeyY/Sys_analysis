import numpy as np


def compute_entropy(probabilities: np.ndarray) -> float:
    return -np.sum(p * np.log2(p) for p in probabilities.flatten() if p > 0)


def main(matrix: np.ndarray) -> tuple[float, float, float, float, float]:
    total_elements = matrix.sum()
    joint_probability = matrix / total_elements
    row_sums = joint_probability.sum(axis=1)
    col_sums = joint_probability.sum(axis=0)
    joint_entropy = compute_entropy(joint_probability)
    row_entropy = compute_entropy(row_sums)
    col_entropy = compute_entropy(col_sums)
    conditional_entropy = 0.0
    for i, row in enumerate(joint_probability):
        if row_sums[i] > 0:
            conditional_entropy += row_sums[i] * compute_entropy(row / row_sums[i])
    mutual_information = col_entropy - conditional_entropy
    return tuple(map(lambda x: round(x, 2), (joint_entropy, row_entropy, col_entropy, conditional_entropy, mutual_information)))


if __name__ == "__main__":
    data = [
        [20, 15, 10, 5],
        [30, 20, 15, 10],
        [25, 25, 20, 15],
        [20, 20, 25, 20],
        [15, 15, 30, 25]
    ]
    matrix = np.array(data)
    result = main(matrix)
    print(result)
