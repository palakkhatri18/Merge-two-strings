class Solution:
    def merge(self, S1, S2):
        # code here
        s=""
        t=len(S1)+len(S2)
        for i in range(t):
            if i<len(S1):
                s+=S1[i]
                
            if i<len(S2):
                s+=S2[i]
        return s 