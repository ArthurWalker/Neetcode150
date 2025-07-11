class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        l, r = 0, n - 1
        # Keep searching, once it reached the final condition, that is where we insert
        while l <= r:
            mid = (r + l) // 2
            val_m = intervals[mid]

            if val_m[0] < target:
                l = mid + 1
            else:
                r = mid - 1

        intervals = intervals[:l] + [newInterval] + intervals[l:]

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res