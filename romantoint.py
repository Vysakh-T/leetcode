class Solution(object):
    def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        sum = 0
        i = 0

        while(i < len(s)):
            if(i+1==len(s)):
                    sum+=val[s[i]]
                    break    

            if s[i]=="I":
                if s[i+1]=="V" or s[i+1]=="X":
                    sum += (val[s[i+1]]-val[s[i]])
                    i+=2
                else:
                    sum+=val[s[i]]
                    i+=1
            elif s[i]=="X":
                if s[i+1]=="L" or s[i+1]=="C":
                    sum += (val[s[i+1]]-val[s[i]])
                    i+=2
                else:
                    sum+=val[s[i]]
                    i+=1
            elif s[i]=="C":
                if s[i+1]=="D" or s[i+1]=="M":
                    sum += (val[s[i+1]]-val[s[i]])
                    i+=2
                else:
                    sum+=val[s[i]]
                    i+=1
            else:
                sum+=val[s[i]]
                i+=1

        return sum
