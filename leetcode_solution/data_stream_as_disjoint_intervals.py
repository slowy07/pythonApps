class SummaryRanges:

    def __init__(self):
        self.interval = []        

    def addNum(self, val: int) -> None:
        self.interval = self.LC57(self.interval,[val,val])

    def getIntervals(self) -> List[List[int]]:
        return self.interval
    def LC57(self, interval, newInterval):
        l = newInterval[0]
        r = newInterval[0]
        flag = 0
        merge = []        
        for t in interval:
            if t[1] + 1 < l:
                merge.append(t)
            elif t[0] > r + 1:
                if flag == 0:
                    merge.append([l,r])
                    flag = 1
                merge.append(t)
            else:   
                l = min(l,t[0])
                r = max(r,t[1])
        if flag == 0:
            merge.append([l,r])
        return merge    

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
