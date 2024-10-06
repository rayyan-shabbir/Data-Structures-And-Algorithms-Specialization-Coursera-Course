def find_approx_matches(k, t, p):
    n, m = len(t), len(p)
    matches = []
    
    for i in range(n - m + 1):
        mismatches = 0
        for j in range(m):
            if t[i + j] != p[j]:
                mismatches += 1
            if mismatches > k:
                break
        if mismatches <= k:
            matches.append(i)
    
    return matches

def main():
    while True:
        try:
            # Reading input
            line = input().strip()
            if not line:
                break
            k, t, p = line.split()
            k = int(k)
            
            # Finding matches
            matches = find_approx_matches(k, t, p)
            print(len(matches), ' '.join(map(str, matches)))
        
        except EOFError:
            break

if __name__ == "__main__":
    main()
