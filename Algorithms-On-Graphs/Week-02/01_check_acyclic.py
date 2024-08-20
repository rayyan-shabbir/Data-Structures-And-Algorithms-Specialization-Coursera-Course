def explore(visited, x, adj):
    if visited[x][0]:
        if not visited[x][1]:
            return 1
    else:
        visited[x][0] = True
        for i in adj[x]:
            if explore(visited, i, adj):
                return 1
        visited[x][1] = True
    return 0


def acyclic(visited, n, adj):
    for i in range(n):
        if not visited[i][0]:
            visited[i][0] = True
            for a in adj[i]:
                if explore(visited, a, adj):
                    return 1
            visited[i][1] = True
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    adj = [[] for _ in range(n)]
    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    
    visited = [[False, False] for _ in range(n)]
    
    print(acyclic(visited, n, adj))