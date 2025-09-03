import heapq
import math

# Directions for 8-directional movement (horizontally, vertically, and diagonally)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Helper function to calculate Euclidean distance heuristic
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Helper function to calculate Manhattan distance heuristic
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Best First Search (Greedy Search) Algorithm
def best_first_search(grid, heuristic):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1, []

    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    came_from = {}
    visited = set()
    visited.add(start)
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return len(path), path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
    
    return -1, []

# A* Search Algorithm
def a_star_search(grid, heuristic):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1, []

    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), start))  # f = g + h
    g_costs = {start: 0}
    came_from = {}
    visited = set()
    visited.add(start)

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return len(path), path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = g_costs[current] + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return -1, []

# Main function to compare both algorithms
def compare_algorithms(grid):
    # Best First Search (Greedy Search)
    print("Best First Search:")
    path_length, path = best_first_search(grid, manhattan_distance)
    if path_length == -1:
        print("Path length: -1")
    else:
        print(f"Path length: {path_length}, Path: {path}")
    
    # A* Search
    print("A* Search:")
    path_length, path = a_star_search(grid, manhattan_distance)
    if path_length == -1:
        print("Path length: -1")
    else:
        print(f"Path length: {path_length}, Path: {path}")
<<<<<<< HEAD

# Example usage
grid1 = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]

print("Example 1:")
compare_algorithms(grid1)

print("\nExample 2:")
compare_algorithms(grid2)

print("\nExample 3:")
compare_algorithms(grid3)
=======
>>>>>>> 61c25c7 (commit)

# Example usage
grid1 = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]

<<<<<<< HEAD
=======
print("Example 1:")
compare_algorithms(grid1)

print("\nExample 2:")
compare_algorithms(grid2)

print("\nExample 3:")
compare_algorithms(grid3)

>>>>>>> 61c25c7 (commit)
