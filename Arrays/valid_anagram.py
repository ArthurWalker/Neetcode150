class Solution:
    def create_dict(self,s: str):
        dicta = {}
        for letter in s:
            if letter not in dicta:
                dicta[letter] = 1
            else:
                dicta[letter]+=1
        return dicta

    def isAnagram(self, s: str, t: str) -> bool:
        dictaS = self.create_dict(s)
        dictaT = self.create_dict(t)
        if dictaS == dictaT:
            return True
        return False
