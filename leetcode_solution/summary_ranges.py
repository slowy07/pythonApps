import itertools
import re

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        return [re.sub('->.*>', '->', '->'.join(repr(n) for _, n in g)) for _, g in itertools.groupby(enumerate(nums), lambda i_n: i_n[1] - i_n[0])]
        
