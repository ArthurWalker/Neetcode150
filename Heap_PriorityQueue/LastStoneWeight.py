class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        stones = stones[::-1]
        while len(stones) > 1:
            remain = stones[0]
            subs = abs(remain - stones[1])
            if len(stones[2:]):
                stones = [subs] + stones[2:]
            else:
                stones = [subs]
            stones.sort()
            stones = stones[::-1]
        return stones[-1]
