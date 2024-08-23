n = int(input())
input_string=input()
k = list(map(int, input_string.split()))
n1 = int(input())
input_string2=input()
q = list(map(int, input_string2.split()))
k.sort()


def binary_search(k, q):
    left_index = 0
    right_index = n - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        
        if k[middle_index] == q:
            return middle_index
        elif k[middle_index] < q:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    
    return -1  # Element not found


final_list=""
for element in q:
    
    i=binary_search(k,element)
    i=str(i)
    final_list+=i+" "

print(final_list)
    



    
    
