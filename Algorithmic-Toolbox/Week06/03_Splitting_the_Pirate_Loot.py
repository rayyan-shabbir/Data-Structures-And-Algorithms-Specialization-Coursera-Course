def can_partition_into_three_subsets(nums):
    total_sum = sum(nums)
    
    # If the total sum is not divisible by 3, we cannot partition it into three subsets with equal sum
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3
    n = len(nums)
    
    # Create a DP table to check possible subset sums
    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    
    # Base case: dp[0][0][0] = True, because with no items, the sum 0 can be achieved with all three subsets
    dp[0][0][0] = True
    
    for i in range(1, n + 1):
        current_val = nums[i - 1]
        for j in range(target + 1):
            for k in range(target + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= current_val:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j - current_val][k]
                if k >= current_val:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j][k - current_val]
    
    # Check if we can partition the array into three subsets with equal sum
    return 1 if dp[n][target][target] else 0

# Example usage
n = int(input())  # Number of items
nums = list(map(int, input().split()))  # Values of the items

result = can_partition_into_three_subsets(nums)
print(result)
