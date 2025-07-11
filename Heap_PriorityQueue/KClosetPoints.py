class Solution:
    def distance(self,x,y):
        from math import sqrt
        squrr = sqrt(x**2+y**2)
        return squrr

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_point = [[self.distance(point[0],point[1]),point] for point in points]
        print(dis_point)
        dis_point.sort(key = lambda x: x[0])
        k_items = dis_point[:k]
        print(k_items)
        return [val[1] for val in k_items]