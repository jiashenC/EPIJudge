import collections
import copy
import functools

from collections import deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    visited = dict()
    queue = deque([(None, s)])
    while len(queue) > 0:
        pre, cur = queue.popleft()
        visited[cur] = pre
        if cur == e:
            break
        for n in neighbors(maze, cur):
            if n not in visited and maze[n.x][n.y] == WHITE:
                queue.append((cur, n))
    if e not in visited:
        return []
    cur, path = e, []
    while cur is not None:
        path.append(cur)
        cur = visited[cur]
    return path[::-1]


def neighbors(maze, s):
    nb = []
    if s.x > 0:
        nb.append(Coordinate(s.x - 1, s.y))
    if s.x < len(maze) - 1:
        nb.append(Coordinate(s.x + 1, s.y))
    if s.y > 0:
        nb.append(Coordinate(s.x, s.y - 1))
    if s.y < len(maze[0]) - 1:
        nb.append(Coordinate(s.x, s.y + 1))
    return nb


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
