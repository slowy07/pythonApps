import operator

from collections import defaultdict, Counter
from itertools import izip, imap

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum(imap(operator.eq, secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        
        return "%dA%dB" % (A, B)
