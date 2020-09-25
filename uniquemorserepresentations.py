class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = set([])
        for i in words:
            cd = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            temp = ""
            for j in i:
                temp += cd[(ord(j)-97)]
            res.add(temp)
        return len(res)