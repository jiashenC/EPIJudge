from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    """
        Construct a table
        2           1, 1
        2,3         1, 2
        2,3,7       1, 3

        that each row stores number of combinations that reach to this score with those digits
    """
    table = [[0 for _ in range(final_score + 1)] for _ in range(len(individual_play_scores))]
    for i in range(len(individual_play_scores)):
        table[i][0] = 1
    for score in range(1, final_score + 1):
        for i, play_score in enumerate(individual_play_scores):
            if score - play_score >= 0:
                table[i][score] += table[i][score - play_score]
            if i >= 1:
                table[i][score] += table[i - 1][score]
    return table[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
