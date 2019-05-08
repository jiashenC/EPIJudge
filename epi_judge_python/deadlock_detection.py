import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import defaultdict


class GraphVertex:
    def __init__(self):
        self.edges = []


def is_deadlocked(graph):
    VISITED, UNSEEN, SEEN = 0, 1, 2
    status = defaultdict(lambda: UNSEEN)

    def has_cycle(cur):
        if status[cur] == SEEN:
            return True
        if status[cur] == VISITED:
            return False
        status[cur] = SEEN

        cycle = False
        for vertex in cur.edges:
            cycle |= has_cycle(vertex)
        status[cur] = VISITED
        return cycle

    return any(has_cycle(n) for n in graph)

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
