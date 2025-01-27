from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Create a graph and a degree dictionary
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}  # Initialize in-degree for all characters

    # Step 2: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        # Check for invalid input: prefix case
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return ""

        # Compare characters and establish edges
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    in_degree[char2] += 1
                break

    # Step 3: Topological Sort using BFS (Kahn's Algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])  # Start with nodes with 0 in-degree
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all characters, return the order
    if len(order) == len(in_degree):
        return "".join(order)
    else:
        return ""  # There is a cycle, so no valid ordering exists

