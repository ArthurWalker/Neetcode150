class Solution:

    def squartRoot(self,pointx,pointy):
        from math import sqrt
        return sqrt(pointx**2+pointy**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = [[self.squartRoot(point[0],point[1]),point[0],point[1]] for point in points]

        heapq.heapify(dist) # Heap is like sort of key function, it will sort by first element of a list
        res = []
        while k > 0:
            distt,x,y = heapq.heappop(dist)
            res.append([x,y])
            k-=1

        return res
        

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