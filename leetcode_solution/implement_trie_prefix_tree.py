class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix)

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None

        return cur


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
