class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
       
        new_stones = [-1 *i for i in stones]
        heapq.heapify(new_stones)
        while len(new_stones)>1:
            print(new_stones)
            top_val1 = heapq.heappop(new_stones)
            top_val2 = heapq.heappop(new_stones)
            diff = top_val1-top_val2
            if top_val2 > top_val1:
                heapq.heappush(new_stones,top_val1-top_val2)
        new_stones.append(0)
        return abs(new_stones[0])


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         if len(stones) == 1:
#             return stones[0]
#         stones.sort()
#         stones = stones[::-1]
#         while len(stones) > 1:
#             remain = stones[0]
#             subs = abs(remain - stones[1])
#             if len(stones[2:]):
#                 stones = [subs] + stones[2:]
#             else:
#                 stones = [subs]
#             stones.sort()
#             stones = stones[::-1]
#         return stones[-1]
