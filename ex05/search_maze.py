from collections import deque

def read_maze(filename: str) -> list[str]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """
    maze = []
    with open(filename, "r") as file:
        maze = file.readlines()
    return maze


def find_start_and_target(maze: list[str]) -> tuple[int, int]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    result = ()
    for line in maze:
        if 'S' in line:
            coordinatesS = []
            coordinatesS.append(line.index('S'))
            coordinatesS.append(maze.index(line))
            updated_result = list(result)
            updated_result.append(coordinatesS)
            result = tuple(updated_result)
        if 'T' in line:
            coordinatesT = []
            coordinatesT.append(line.index('T'))
            coordinatesT.append(maze.index(line))
            updated_result = list(result)
            updated_result.append(coordinatesT)
            result = tuple(updated_result)
    return result



def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in directions:
        new_x = position[0] + x
        new_y = position[1] + y
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))
    return neighbors


def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        current_position, path = queue.popleft()
        if current_position == target:
            return path
        for neighbor in get_neighbors(maze, current_position):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []


def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        current_position, path = stack.pop()
        if current_position == target:
            return path
        for neighbor in get_neighbors(maze, current_position):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return []


def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    for r, row in enumerate(maze):
        row_str = ""
        for c, char in enumerate(row):
            if char == 'S':
                row_str += '\033[93m' + 'S' + '\033[0m'
            elif char == 'T':
                row_str += '\033[92m' + 'T' + '\033[0m'
            elif (r, c) in path and char not in ('S', 'T'):
                row_str += '\033[91m' + '.' + '\033[0m'
            else:
                row_str += char
        print(row_str)
