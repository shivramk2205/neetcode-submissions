class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        mpp={}
        for i in s:
            mp[i]=mp.get(i,0)+1
        for j in t:
            mpp[j]=mpp.get(j,0)+1
        return mp==mpp
        