import heapq
import math

# 8 directions (up, down, left, right + diagonals)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

# Heuristic function 
def heuristic(x, y, goal):
    return math.sqrt((x - goal[0]) ** 2 + (y - goal[1]) ** 2)


# Best First Search (Greedy)
def best_first_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    
    
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = []  
    heapq.heappush(pq, (heuristic(0, 0, goal), start))
    visited = set()
    parent = {start: None}

    while pq:
        _, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            
            path = []
            while (x, y) is not None:
                path.append((x, y))
                (x, y) = parent[(x, y)]
            return len(path), path[::-1]

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                parent[(nx, ny)] = (x, y)
                heapq.heappush(pq, (heuristic(nx, ny, goal), (nx, ny)))

    return -1, []



# A* Search

def a_star_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)

    # If start or goal is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = []  # priority queue
    heapq.heappush(pq, (0 + heuristic(0, 0, goal), 0, start))  # (f, g, node)
    parent = {start: None}
    g_cost = {start: 0}

    while pq:
        f, g, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            
            path = []
            while (x, y) is not None:
                path.append((x, y))
                (x, y) = parent[(x, y)]
            return len(path), path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                new_g = g + 1
                if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_g
                    parent[(nx, ny)] = (x, y)
                    f = new_g + heuristic(nx, ny, goal)
                    heapq.heappush(pq, (f, new_g, (nx, ny)))

    return -1, []



# Example Test Cases

if __name__ == "__main__":
    grids = [
        [[0, 1],
         [1, 0]],

        [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 0]],

        [[1, 0, 0],
         [1, 1, 0],
         [1, 1, 0]]
    ]

    for i, grid in enumerate(grids, 1):
        print(f"\nExample {i}:")
        bf_len, bf_path = best_first_search(grid)
        print(f"Best First Search  → Path length: {bf_len}, Path: {bf_path}")
        a_len, a_path = a_star_search(grid)
        print(f"A* Search          → Path length: {a_len}, Path: {a_path}")

