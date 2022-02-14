import operator
from collections import Counter, defaultdict
from itertools import imap, izip


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
