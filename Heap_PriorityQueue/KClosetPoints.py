class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_max = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        # Remove (n-k) min elements to keep only the k largest items currently
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # Remove top item (which is the smallest) of self.minHeap

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val) # Push an item to self.minHeap and rearrange
        if len(self.minHeap) > self.k_max:
            heapq.heappop(self.minHeap) # Remove to maintain top k items
        return self.minHeap[0]


# class Solution:
#     def distance(self,x,y):
#         from math import sqrt
#         squrr = sqrt(x**2+y**2)
#         return squrr

#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         dis_point = [[self.distance(point[0],point[1]),point] for point in points]
#         print(dis_point)
#         dis_point.sort(key = lambda x: x[0])
#         k_items = dis_point[:k]
#         print(k_items)
#         return [val[1] for val in k_items]