class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_max = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        self.nums = self.nums[::-1]
        print(self.nums)
        return self.nums[self.k_max-1]
