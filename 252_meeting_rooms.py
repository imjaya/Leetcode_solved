class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i:i[0])
        if(len(intervals)==0 or len(intervals)==1):
            return True
        a=intervals[0]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<a[1]):
                return False
            else:
                a=intervals[i]
        return True