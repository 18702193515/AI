"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(maze, n, m):
    visited = set()
    visited.add((0, 0))
    memory = [(0, 0, 0)]
    queue = [(0, 0, 0)]  # (row, col, steps)
    parents = [[None] * m for _ in range(n)]
    path = []
    while queue:
        row, col, steps = queue.pop(0)
        if (row, col) == (n - 1, m - 1):
            path.append((row, col, steps))
            print(steps)
            while steps:
                steps -= 1
                row, col = parents[row][col]
                path.append((row, col, steps))
            path.reverse()
            return path, memory
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                memory.append((new_row, new_col, steps + 1))
                queue.append((new_row, new_col, steps + 1))
                parents[new_row][new_col] = (row, col)


def visualize_maze_with_path(maze, path, interval, memory):
    if path:
        path_x, path_y, steps = zip(*path)
        plt.figure(figsize=(len(maze[0])/2, len(maze)/2))
        plt.imshow(maze, cmap='Greys', interpolation='nearest')

        new_colored_cells = []

        for i in range(len(path)):
            plt.plot(path_y[:i + 1], path_x[:i + 1], marker='o',
                     markersize=8, color='red', linewidth=3)

            for x, y in new_colored_cells:
                color = 'yellow'
                plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                 x + 0.5, color=color, alpha=0.5)

            new_colored_cells.clear()

            for x, y, step in memory:
                if step == i: 
                    color = 'blue'
                    new_colored_cells.append((x, y))
                    plt.fill_between([y - 0.5, y + 0.5], x - 0.5,
                                     x + 0.5, color=color, alpha=0.5)

            plt.xticks(range(len(maze[0])))
            plt.yticks(range(len(maze)))
            plt.gca().set_xticks(
                [x - 0.5 for x in range(1, len(maze[0]))], minor=True)
            plt.gca().set_yticks(
                [y - 0.5 for y in range(1, len(maze))], minor=True)
            plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
            plt.axis('on')
            plt.pause(interval)
        plt.show()


interval = 0.25

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

path, memory = bfs(maze, n, m)
visualize_maze_with_path(maze, path, interval, memory)


# 15 15
# 0 0 0 1 0 0 1 0 0 0 0 1 1 1 1 
# 1 0 0 0 1 0 1 0 1 1 0 0 0 0 0 
# 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 
# 1 0 0 0 1 0 1 1 0 0 0 0 0 1 0
# 1 0 1 0 0 0 0 1 0 1 0 1 0 0 1
# 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0
# 0 1 0 0 0 1 0 0 0 1 0 0 1 1 0
# 0 1 0 0 1 0 0 1 0 0 1 0 1 0 0 
# 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 
# 0 1 0 0 1 0 1 0 0 1 0 0 1 1 0
# 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1
# 0 1 0 1 1 0 1 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
# 1 0 1 0 1 1 0 1 1 0 0 0 0 0 0
# 1 0 1 0 0 0 0 0 0 1 0 1 1 0 0

