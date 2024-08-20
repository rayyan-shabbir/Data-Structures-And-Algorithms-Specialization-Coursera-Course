def topological_sort_dfs(adj, n):
    visited = [False] * n
    stack = []

    def dfs(v):
        visited[v] = True

        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor)
    
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    
    stack = topological_sort_dfs(adj, n)
    

    while stack:
        print(stack.pop() + 1, end=' ')
    print()
