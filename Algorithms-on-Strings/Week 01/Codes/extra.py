# python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_pattern


class Trie:
    def __init__():
        self.root = TrieNode()

    def insert_pattern(self, pattern):
        curNode = self.root

        for p in pattern:
            if p not in curNode.children:
                curNode.children[p] = TrieNode()
            
            curNode = curNode.children[]