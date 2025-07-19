class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        shouldFillFirstRow = 0 in matrix[0]
        shouldFillFirstCol = 0 in [row[0] for row in matrix]

        # Mark zeroes on first row and column for other rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Use marks to set zeroes, excluding first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if shouldFillFirstRow:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if shouldFillFirstCol:
            for i in range(m):
                matrix[i][0] = 0
