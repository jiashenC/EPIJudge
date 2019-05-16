import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    visited = [set([]), set([])]
    queue = deque([(0, graph[0])])
    remaining = set(graph)
    while len(queue) > 0 or len(remaining) > 0:
        if len(queue) <= 0 and len(remaining) > 0:
            vertex = remaining.pop()
            remaining.add(vertex)
            queue = deque([(0, vertex)])

        idx, vertex = queue.popleft()
        if vertex in visited[1 - idx]:
            return False
        if vertex in visited[idx]:
            continue
        visited[idx].add(vertex)
        remaining.remove(vertex)
        for n in vertex.edges:
            queue.append((1 - idx, n))
    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
