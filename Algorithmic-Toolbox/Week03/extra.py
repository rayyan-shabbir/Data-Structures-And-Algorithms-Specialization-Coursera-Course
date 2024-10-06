from functools import cmp_to_key

def compare(a, b):
    # Compare two numbers by comparing their concatenated results in both possible orders
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def maximize_salary(numbers):
    # Convert all numbers to strings for easy concatenation
    numbers_str = list(map(str, numbers))
    
    # Sort the numbers using the custom comparator
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))
    
    # Concatenate the sorted numbers
    return ''.join(sorted_numbers)

# Example usage
numbers = list(map(int, input().split()))
result = maximize_salary(numbers)
print(result)
