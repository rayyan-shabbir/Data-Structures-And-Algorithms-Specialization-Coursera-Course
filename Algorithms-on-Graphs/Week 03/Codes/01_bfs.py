import queue

def distance(n, adj, s, t):
    visited = [False] * n
    dist = [-1] * n
    q = queue.Queue()
    q.put(s)
    visited[s] = True
    dist[s] = 0
    
    if s == t:
        return 0
    
    while not q.empty():
        x = q.get()
        for i in adj[x]:
            if i == t:
                return dist[x] + 1
            if not visited[i]:
                q.put(i)
                dist[i] = dist[x] + 1
                visited[i] = True
    
    return -1

if __name__ == '__main__':
    # Read the number of nodes and edges
    n, m = map(int, input().split())
    
    # Initialize adjacency list
    adj = [[] for _ in range(n)]
    
    # Read the edges and populate the adjacency list
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    # Read the source and target nodes
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    
    # Compute and print the shortest path distance
    print(distance(n, adj, s, t))
