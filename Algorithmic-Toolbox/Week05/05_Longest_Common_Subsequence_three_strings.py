def lcs_of_three(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)

    # Create a 3D array to store lengths of LCS
    L = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the L[m+1][n+1][o+1] in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(L[i - 1][j][k], L[i][j - 1][k], L[i][j][k - 1])

    # L[m][n][o] contains the length of LCS of X, Y, Z
    return L[m][n][o]

# Example usage with integer sequences
# Length of first sequence
n = int(input())  
# First sequence
X = list(map(int, input().split()))  
# Length of second sequence
m = int(input())  
# Second sequence
Y = list(map(int, input().split())) 
# Length of third sequence
l = int(input())  
# Third sequence
Z = list(map(int, input().split()))  

# Get the length of the LCS of the three sequences
lcs_length = lcs_of_three(X, Y, Z)
print(lcs_length)
