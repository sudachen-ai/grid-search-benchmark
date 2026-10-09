import heapq
import time


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


def dijkstra(grid_obj):
    start = grid_obj.start
    goal = grid_obj.goal

    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}
    expanded_nodes = 0

    start_time = time.time()

    while pq:
        current_cost, current = heapq.heappop(pq)
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
            new_cost = cost_so_far[current] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))

    end_time = time.time()
    return {
        "path": None,
        "path_length": -1,
        "expanded_nodes": expanded_nodes,
        "runtime": end_time - start_time,
    }