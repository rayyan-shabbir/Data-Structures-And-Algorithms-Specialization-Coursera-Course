def main():
    M = 1000000001
    sorted_set = set()
    last_sum_result = 0
    results = []

    def add(i):
        value = (i + last_sum_result) % M
        sorted_set.add(value)
    
    def delete(i):
        value = (i + last_sum_result) % M
        sorted_set.discard(value)
    
    def find(i):
        value = (i + last_sum_result) % M
        if value in sorted_set:
            results.append("Found")
        else:
            results.append("Not found")
    
    def range_sum(l, r):
        l_val = (l + last_sum_result) % M
        r_val = (r + last_sum_result) % M
        
        sorted_list = sorted(sorted_set)
        
        # Ensure l_val <= r_val
        if l_val <= r_val:
            sum_result = sum(x for x in sorted_list if l_val <= x <= r_val)
        else:
            sum_result = sum(x for x in sorted_list if x >= l_val) + sum(x for x in sorted_list if x <= r_val)
        
        results.append(str(sum_result))
        return sum_result
    
    # Read number of operations
    n = int(input().strip())
    
    # Process each operation
    for _ in range(n):
        operation = input().strip().split()
        op_type = operation[0]
        a = int(operation[1])
        
        if op_type == '+':
            add(a)
        elif op_type == '-':
            delete(a)
        elif op_type == '?':
            find(a)
        elif op_type == 's':
            last_sum_result = range_sum(a, int(operation[2]))
    
    # Print all results
    print("\n".join(results))

if __name__ == "__main__":
    main()
