class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs,key=len)
        s = strs[0]+" "
        while(s):
            s = s[:-1]
            i = 0
            while(i<len(strs)):
                if s != strs[i][:len(s)]:
                    break
                i+=1
            if i==len(strs):
                return s
            else:
                continue
        return ""
