from collections import deque

people = {'Srikar': 5, 'Suprith': 10, 'Mahesh': 20}
all_people = set(people.keys())

initial_state = (frozenset(all_people), frozenset(), 'left', 0)

def is_goal(state):
    return state[0] == frozenset() and state[1] == frozenset(all_people)

def get_next_states(state):
    left, right, torch_side, time_elapsed = state
    next_states = []
    if torch_side == 'left':
        movers = list(left)
        for i in range(len(movers)):
            for j in range(i, len(movers)):
                pair = {movers[i]}
                if i != j:
                    pair.add(movers[j])
                time = max(people[p] for p in pair)
                new_left = left - pair
                new_right = right | pair
                new_state = (frozenset(new_left), frozenset(new_right), 'right', time_elapsed + time)
                next_states.append(new_state)
    else:
        movers = list(right)
        for p in movers:
            time = people[p]
            new_left = left | {p}
            new_right = right - {p}
            new_state = (frozenset(new_left), frozenset(new_right), 'left', time_elapsed + time)
            next_states.append(new_state)
    return next_states

def bfs_bridge():
    queue = deque()
    visited = set()
    queue.append((initial_state, [initial_state]))
    while queue:
        current, path = queue.popleft()
        if is_goal(current):
            return path
        state_key = (current[0], current[1], current[2])
        if state_key in visited:
            continue
        visited.add(state_key)
        for next_state in get_next_states(current):
            if next_state[3] <= 35:
                queue.append((next_state, path + [next_state]))
    return []

def dfs_bridge(state, path, visited):
    if is_goal(state):
        return path
    state_key = (state[0], state[1], state[2])
    if state_key in visited:
        return None
    visited.add(state_key)
    for next_state in get_next_states(state):
        if next_state[3] <= 35:
            result = dfs_bridge(next_state, path + [next_state], visited)
            if result:
                return result
    return None

print("\nBridge Crossing - BFS:")
bfs_result = bfs_bridge()
for step in bfs_result:
    print(step)
if bfs_result:
    print(f"Total Time: {bfs_result[-1][3]} minutes")
else:
    print("No solution found with BFS.")

print("\nBridge Crossing - DFS:")
dfs_result = dfs_bridge(initial_state, [initial_state], set())
if dfs_result:
    for step in dfs_result:
        print(step)
    print(f"Total Time: {dfs_result[-1][3]} minutes")
else:
    print("No solution found with DFS.")

