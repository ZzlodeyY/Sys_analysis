import numpy as np

# Исходная матрица данных
data = [
    [20, 15, 10, 5],
    [30, 20, 15, 10],
    [25, 25, 20, 15],
    [20, 20, 25, 20],
    [15, 15, 30, 25]
]

matrix = np.array(data)
total_elements = matrix.sum()

# Подсчет вероятностей
joint_probability = matrix / total_elements
row_sums = joint_probability.sum(axis=1)
col_sums = joint_probability.sum(axis=0)

def compute_entropy(probabilities):
    """Рассчитывает энтропию для заданного массива вероятностей."""
    return -sum(p * np.log2(p) for p in probabilities.flatten() if p > 0)

# Энтропия для совместного распределения
joint_entropy = compute_entropy(joint_probability)

# Энтропия для маргинальных распределений
row_entropy = compute_entropy(row_sums)
col_entropy = compute_entropy(col_sums)

# Количество информации
mutual_information = row_entropy + col_entropy - joint_entropy

# Вывод результатов
print(f"Количество информации I(X, Y): {mutual_information:.2f}")
print(f"Энтропия совместного события H(XY): {joint_entropy:.2f}")
