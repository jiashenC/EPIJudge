from test_framework import generic_test
import collections


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    matrix = collections.defaultdict(lambda: [])
    words = list(D)
    for k, w1 in enumerate(words):
        for w2 in words[k:]:
            diff = 0
            for i in range(len(w1)):
                diff += 1 if w1[i] != w2[i] else 0
                if diff > 1:
                    break
            if diff <= 1:
                matrix[w1].append(w2)
                matrix[w2].append(w1)

    visited = set([])
    queue = collections.deque([(0, s)])
    while queue:
        dis, word = queue.popleft()
        if word in visited:
            continue
        if word == t:
            return dis
        visited.add(word)
        for next in matrix[word]:
            queue.append((dis + 1, next))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
