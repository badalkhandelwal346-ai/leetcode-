class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1=startTime[0:2]
        h2=endTime[0:2]
        m1=startTime[3:5]
        m2=endTime[3:5]
        s1=startTime[6:8]
        s2=endTime[6:8]
        ans1=(int(h1)*60*60)+int(m1)*60+int(s1)
        ans2=(int(h2)*60*60)+int(m2)*60+int(s2)
        return ans2-ans1