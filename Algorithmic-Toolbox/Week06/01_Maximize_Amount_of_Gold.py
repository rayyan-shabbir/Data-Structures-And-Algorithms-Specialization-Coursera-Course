def knapsack(W, weights):
    n = len(weights)

    # Create a 2D DP array with dimensions (n+1) x (W+1)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the DP array
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # Don't include the ith item
            dp[i][w] = dp[i - 1][w]  
            # Include the ith item, if it fits
            if weights[i - 1] <= w:  
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])

    # The value in dp[n][W] is the maximum weight that can be packed
    return dp[n][W]

# Example usage
# Capacity of the backpack and number of gold bars
W, n = map(int, input().split())  
# Weights of the gold bars
weights = list(map(int, input().split()))  

max_weight = knapsack(W, weights)
print(max_weight)
