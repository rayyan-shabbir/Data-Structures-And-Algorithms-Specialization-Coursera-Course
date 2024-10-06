import queue

def bipartite(adj, n):
    partition = [None] * n
    q = queue.Queue()
    
    # Start BFS from the first node
    for start in range(n):
        # Check if this node is not yet visited
        if partition[start] is None:  
            q.put(start)
            partition[start] = 'Black'
            while not q.empty():
                x = q.get()
                for i in adj[x]:
                    if partition[i] is None:
                        # Assign the opposite color to the adjacent node
                        if partition[x] == 'Black':
                            partition[i] = 'White'
                        else:
                            partition[i] = 'Black'
                        q.put(i)
                    elif partition[i] == partition[x]:
                        # If adjacent node has the same color, graph is not bipartite
                        return 0
    return 1

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
    
    # Check if the graph is bipartite and print the result
    print(bipartite(adj, n))
