def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of LCS
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L[m+1][n+1] in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS for X[0..m-1], Y[0..n-1]
    length_of_lcs = L[m][n]

    # To print the LCS, we need to backtrack
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_sequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The lcs_sequence contains the LCS in reverse order, so reverse it
    lcs_sequence.reverse()

    return lcs_sequence, length_of_lcs

# Example usage with integer sequences
n = int(input())  # Length of first sequence
X = list(map(int, input().split()))  # First sequence
m = int(input())  # Length of second sequence
Y = list(map(int, input().split()))  # Second sequence

lcs_seq, lcs_length = lcs(X, Y)
print(lcs_length)
# print("A common subsequence of length", lcs_length, "is", tuple(lcs_seq))
