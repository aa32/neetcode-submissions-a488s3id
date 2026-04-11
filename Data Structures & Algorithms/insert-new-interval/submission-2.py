class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n==0:
            return [newInterval]
        left = 0
        right = n-1
        target = newInterval[0]

        while(left <=right):
            mid = (left+right)//2
            if intervals[left][0]<target:
                left+=1
            else:
                right -=1

        
        intervals.insert(left,newInterval)


        res = []
        for interval in intervals:
            if len(res)>0 and interval[0]<=res[-1][1] :
                res[-1][1] = max(interval[1],res[-1][1])

            else:
                res.append(interval)

        return res
            


            