class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        best_i = values[0] + 0  # values[i] + i

        for j in range(1, len(values)):
            # calculate score for pair (i, j)
            max_score = max(max_score, best_i + values[j] - j)
            # update best_i for next iteration
            best_i = max(best_i, values[j] + j)

        return max_score
