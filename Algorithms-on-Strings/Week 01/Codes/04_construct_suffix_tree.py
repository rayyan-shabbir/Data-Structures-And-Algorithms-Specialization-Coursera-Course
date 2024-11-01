# python3
from collections import deque


class SuffixTree(object):

    class Node(object):
        def __init__(self, lab):
            # label on path leading to this node
            self.lab = lab 
            # outgoing edges; maps characters to nodes
            self.out = {}  

    def __init__(self, s):
        """ Make suffix tree, without suffix links, from s in quadratic time
            and linear space """

        self.root = self.Node(None)

         # trie for just longest suf
        self.root.out[s[0]] = self.Node(s)
        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(s)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or
                    # until we mismatch , 'k' is for iterarting further in string
                    k = j+1
                    # print('j', j, 'K',k, 'label', child.lab)
                    while k-j < len(lab) and s[k] == lab[k-j]:
                        k += 1

                    # which type of condition in while loop mismatches    
                    if k-j == len(lab):
                        # we exhausted the edge
                        cur = child 
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = lab[k-j], s[k]
                        
                        # create “mid”: new node bisecting edge
                        mid = self.Node(lab[:k-j])

                        # adding new child
                        mid.out[cNew] = self.Node(s[k:])

                        # original child becomes mid’s child
                        child.lab = lab[k-j:]
                        mid.out[cExist] = child

                        # original child’s label is curtailed
                        # print('j-', j, 'label', child.lab)
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def Print(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            u = queue.popleft()
            if u != self.root:
                print(u.lab)
            for label, node in u.out.items():
                queue.append(node)


# Root
#  ├── "p" -> Node("panam$")
#  ├── "a" -> Node("a")
#  │       ├── "n" -> Node("nam$")
#  │       └── "m" -> Node("m$")
#  ├── "n" -> Node("nam$")
#  └── "m" -> Node("m$")


if __name__ =='__main__':
    text = input()
    stree = SuffixTree(text)
    stree.Print()