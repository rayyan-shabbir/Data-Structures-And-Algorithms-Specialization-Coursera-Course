import sys


class DisjointSet(object):
    """Simulates a sequence of merge operations with tables in a database."""


    def __init__(self, n, lines):
        """Initializes a set for given n elements.

        Initially, the set consists of one element which is pointing to itself.
        Also during initialization the rank(tree's height) is assigned to 1
        for each set."""

        self.n = n
        self.lines = [0] + lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)


    def get_max_lines(self):
        return self.lines


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    ds = DisjointSet(n, lines)
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        # ds.merge(destination, source)
        print(ds.get_max_lines())