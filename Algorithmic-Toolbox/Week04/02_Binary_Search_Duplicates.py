n = int(input())
input_string = input()
k = list(map(int, input_string.split()))
n1 = int(input())
input_string2 = input()
q = list(map(int, input_string2.split()))


def binary_search(k, q):
    results = -1
    left_index = 0
    # Use len(k) to get the correct last index
    right_index = len(k) - 1  
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        
        if k[middle_index] == q:
            results = middle_index
            # Continue searching left for the first occurrence
            right_index = middle_index - 1  
        elif k[middle_index] < q:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    
    # Element not found
    return results  

final_list = ""
for element in q:
    i = binary_search(k, element)
    i = str(i)
    final_list += i + " "

# Strip the extra space at the end
print(final_list.strip())  
