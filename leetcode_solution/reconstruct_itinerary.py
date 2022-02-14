import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = collections.defaultdict(list)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        for x in adj.itervalues():
            x.sort(reverse = True)
            
        origin = "JFK"
        result = []
        stk = [origin]
        while stk:
            while adj[stk[-1]]:
                stk.append(adj[stk[-1]].pop())
                
            result.append(stk.pop())
        result.reverse()
        return result

        
