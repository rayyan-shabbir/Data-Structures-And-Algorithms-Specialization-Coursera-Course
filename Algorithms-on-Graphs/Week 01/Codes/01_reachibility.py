def reach(visited, adj, x, y):
    if not visited[x]:
        visited[x] = True
        if adj[x]:
            for i in adj[x]:
                if i == y:
                    return 1
                elif not visited[i]:
                     if reach(visited, adj, i, y):
                         return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        edges.append((x, y))
    
    u, v = map(int, input().split())

    adj = [[] for _ in range(n)]
    visited = [(False) for _ in range(n)]

    u, v = u - 1, v - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(visited, adj, u, v))