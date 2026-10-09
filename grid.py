import random


class Grid:
    def __init__(self, rows=10, cols=10, obstacle_prob=0.2):
        self.rows = rows
        self.cols = cols
        self.obstacle_prob = obstacle_prob
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.goal = None

    def generate(self):
        # 0 = free, 1 = obstacle
        self.grid = [
            [1 if random.random() < self.obstacle_prob else 0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        free_cells = [(r, c) for r in range(self.rows) for c in range(self.cols) if self.grid[r][c] == 0]

        if len(free_cells) < 2:
            return self.generate()

        self.start, self.goal = random.sample(free_cells, 2)
        return self.grid, self.start, self.goal

    def in_bounds(self, node):
        r, c = node
        return 0 <= r < self.rows and 0 <= c < self.cols

    def passable(self, node):
        r, c = node
        return self.grid[r][c] == 0

    def neighbors(self, node):
        r, c = node
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up/down/left/right
        result = []

        for dr, dc in directions:
            nxt = (r + dr, c + dc)
            if self.in_bounds(nxt) and self.passable(nxt):
                result.append(nxt)

        return result

    def print_grid(self, path=None):
        path = set(path) if path else set()

        for r in range(self.rows):
            row_str = []
            for c in range(self.cols):
                pos = (r, c)
                if pos == self.start:
                    row_str.append("S")
                elif pos == self.goal:
                    row_str.append("G")
                elif pos in path:
                    row_str.append("*")
                elif self.grid[r][c] == 1:
                    row_str.append("#")
                else:
                    row_str.append(".")
            print(" ".join(row_str))