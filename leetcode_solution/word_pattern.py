from itertools import izip
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        
        w2p, p2w = {}, {}
        
        for p, w in izip(pattern, words):
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
                
            elif w not in w2p or w2p[w] != p:
                return False
            
        return True
        
