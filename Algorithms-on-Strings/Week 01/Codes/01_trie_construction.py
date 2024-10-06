#python3
def BuildTrie(patterns):
    tree = {}
    new_node = 0
    
    for pattern in patterns:
        current_node = 0
        for i, current_symbol in enumerate(pattern):
            if current_node in tree and current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                new_node += 1
                if current_node not in tree:
                    tree[current_node] = {}
                tree[current_node][current_symbol] = new_node
                current_node = new_node
    return tree


if __name__ == '__main__':
    n_patterns = int(input())
    patterns = [input().strip() for _ in range(n_patterns)]
    tree = BuildTrie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))


