class Solution:

    def encode(self, strs: List[str]) -> str:
        speical = '44*'
        new_sts = ['44*'+item for item in strs]
        return ''.join(new_sts)


    def decode(self, s: str) -> List[str]:
        return s.split('44*')[1:]