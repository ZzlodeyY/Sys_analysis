from collections import deque, defaultdict
import csv

def main(csv_filename: str, answer_csv:str) -> None:
    edges = []
    with open(csv_filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            edges.append(row)
    
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    
    all_nodes = set(node for pair in edges for node in pair)
    
    def bfs(start_node):
        queue = deque([(start_node, 0)])
        visited = set()
        steps_to_leaves = 0
        total_reachable = 0
        while queue:
            node, depth = queue.popleft()
            if node not in visited:
                visited.add(node)
                total_reachable += 1
                if not graph[node]: 
                    steps_to_leaves = max(steps_to_leaves, depth)
                for child in graph[node]:
                    queue.append((child, depth + 1))
        return steps_to_leaves, total_reachable
    
    result = []
    for node in all_nodes:
        steps, reachable = bfs(node)
        result.append(f"{node},{steps},{reachable}")
    
    with open(answer_csv, 'w', newline='') as csvfile:
        csvfile.write('\n'.join(result))

csv_filename = "task2.csv"
answer_csv = 'answer.csv'
main(csv_filename,answer_csv)
