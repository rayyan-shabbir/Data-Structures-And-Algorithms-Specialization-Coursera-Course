# python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_pattern = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root

        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_pattern = True

    def search_in_text(self, text):
        positions = []

        for i in range(len(text)):
            node = self.root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_end_of_pattern:
                    positions.append(i)
                j += 1

        return positions

def find_pattern_positions(text, patterns):
    trie = Trie()

    # root -> {a: T1()}
    # T1() -> {n: T2()}

    for pattern in patterns:
        trie.insert(pattern)


    # print(trie)
    return trie.search_in_text(text)


# Input
text = input()
n_patterns = int(input())
patterns = list(input() for _ in range(n_patterns))

# Find pattern positions
positions = find_pattern_positions(text, patterns)

print(" ".join(map(str, positions)))
