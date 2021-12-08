class Trie(object):
    def __init__(self, endOfWord=False):
        self.child = [None] * 26
        self.endOfWord = endOfWord


class WordDictionary:
    def index(self, c):
        return ord(c) - 97

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if node.child[self.index(word[i])] == None:
                node.child[self.index(word[i])] = Trie()
            node = node.child[self.index(word[i])]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.f(word, node, 0)

    def f(self, word, node, pos):
        if node == None:
            return False
        ans = False
        if pos == len(word):
            return node.endOfWord
        if word[pos] == ".":
            for i in range(26):
                ans = ans or self.f(word, node.child[i], pos + 1)
        else:
            if node.child[self.index(word[pos])] == None:
                ans = False
            else:
                ans = self.f(word, node.child[self.index(word[pos])], pos + 1)
        return ans


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
