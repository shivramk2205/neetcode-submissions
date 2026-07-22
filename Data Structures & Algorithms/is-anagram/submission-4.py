class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        mp={}
        for j in s:
            mp[j]=mp.get(j,0)+1
        
        for j in t:
            if j not in mp:
                return False
            mp[j]-=1
            if mp[j]==0:
                del mp[j]
        return len(mp)==0

        