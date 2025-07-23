from collections import deque

# ---------------- Rabbit Leap Problem ----------------
initial_rabbit = ['E', 'E', 'E', '.', 'W', 'W', 'W']
goal_rabbit = ['W', 'W', 'W', '.', 'E', 'E', 'E']

def get_rabbit_moves(state):
    moves = []
    for i in range(len(state)):
        if state[i] == 'E':
            if i + 1 < 7 and state[i + 1] == '.':
                new = state[:]
                new[i], new[i + 1] = new[i + 1], new[i]
                moves.append(new)
            if i + 2 < 7 and state[i + 1] == 'W' and state[i + 2] == '.':
                new = state[:]
                new[i], new[i + 2] = new[i + 2], new[i]
                moves.append(new)
        elif state[i] == 'W':
            if i - 1 >= 0 and state[i - 1] == '.':
                new = state[:]
                new[i], new[i - 1] = new[i - 1], new[i]
                moves.append(new)
            if i - 2 >= 0 and state[i - 1] == 'E' and state[i - 2] == '.':
                new = state[:]
                new[i], new[i - 2] = new[i - 2], new[i]
                moves.append(new)
    return moves

def bfs_rabbit():
    queue = deque()
    visited = set()
    queue.append((initial_rabbit, [initial_rabbit]))
    while queue:
        curr, path = queue.popleft()
        if curr == goal_rabbit:
            return path
        visited.add(tuple(curr))
        for move in get_rabbit_moves(curr):
            if tuple(move) not in visited:
                queue.append((move, path + [move]))
    return []

def dfs_rabbit(curr, path, visited):
    if curr == goal_rabbit:
        return path
    visited.add(tuple(curr))
    for move in get_rabbit_moves(curr):
        if tuple(move) not in visited:
            result = dfs_rabbit(move, path + [move], visited)
            if result:
                return result
    return []

print("Rabbit Leap - BFS:")
for state in bfs_rabbit():
    print(state)

print("\nRabbit Leap - DFS:")
for state in dfs_rabbit(initial_rabbit, [initial_rabbit], set()):
    print(state)

