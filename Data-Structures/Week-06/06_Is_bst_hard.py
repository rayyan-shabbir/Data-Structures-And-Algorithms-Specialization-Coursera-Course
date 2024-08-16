import sys, threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)

def checkbst(tree, index, min, max):
    if index == -1:
        return True

    if tree[index][0] < min or tree[index][0] >= max:
        return False

    return checkbst(tree, tree[index][1], min, tree[index][0]) and checkbst(tree, tree[index][2], tree[index][0], max)


def IsBinarySearchTree(tree):
    if not tree:
        return True
    res = checkbst(tree, 0,  float('-inf'),  float('inf'))
    return res


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    # print(tree)

    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
