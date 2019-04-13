from test_framework import generic_test


def find_maximum_subarray(A):
    """
        max_sum[i] = max(A[i], max_sum[i - 1] + A[i])
    """
    cur, max_sum = 0, 0
    for num in A:
        cur = max(num, cur + num)
        max_sum = max(max_sum, cur)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
