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


# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k_max = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums.sort()
#         self.nums = self.nums[::-1]
#         print(self.nums)
#         return self.nums[self.k_max-1]
