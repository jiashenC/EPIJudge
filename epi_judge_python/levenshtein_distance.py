from test_framework import generic_test


def levenshtein_distance(A, B):
    """
        len(A) = a, len(B) = b

        if A[a] = B[b]: E[a] = E[a - 1], B[b] = B[b - 1]
        else: 1 + min(deletion, insertion, substitution)
    """
    table = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(len(A) + 1):
        table[i][0] = i
    for i in range(len(B) + 1):
        table[0][i] = i
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j - 1], min(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
