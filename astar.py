import heapq
import time


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return None

    current = goal
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    return path


def astar(grid_obj):
    start = grid_obj.start
    goal = grid_obj.goal

    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {start: None}
    g_cost = {start: 0}
    expanded_nodes = 0

    start_time = time.time()

    while pq:
        _, current = heapq.heappop(pq)
        expanded_nodes += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, start, goal)
            return {
                "path": path,
                "path_length": len(path) - 1 if path else -1,
                "expanded_nodes": expanded_nodes,
                "runtime": end_time - start_time,
            }

        for neighbor in grid_obj.neighbors(current):
            new_g = g_cost[current] + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic(neighbor, goal)
                came_from[neighbor] = current
                heapq.heappush(pq, (f_cost, neighbor))

    end_time = time.time()
    return {
        "path": None,
        "path_length": -1,
        "expanded_nodes": expanded_nodes,
        "runtime": end_time - start_time,
    }