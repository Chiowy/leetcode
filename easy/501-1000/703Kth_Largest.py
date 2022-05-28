from typing import List # 解决NameError: name 'List' is not defined
import heapq

class KthLargest:

    def __init__(self, k: int, nums:List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)  # 将列表nums转换成heap
        print(f'Heap : {self.minHeap}')
        while len(self.minHeap) > k:  # 如果要找到第k大的数，只需要要让heap的长度为k即可
            heapq.heappop(self.minHeap) # it will remove the smallest element from the heap 


    def add(self, val) -> int:
        heapq.heappush(self.minHeap, val)  # 新来的数先入栈
        if len(self.minHeap) > self.k:  # pop出最小的元素
            heapq.heappop(self.minHeap)  
        return self.minHeap[0]

k = KthLargest(3, [1, 2, 3, 2, 5, 1])
print(k.add(3))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)