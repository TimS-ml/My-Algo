from heapq import heapify, heappop, heappush

def test(li):
    heap = []
    heapify(heap)
    for key in li:
        heappush(heap, key)
    
    # for _ in range(len(heap)):
    #     print(heappop(heap))
    for i in heap:
        print(i)


li = [
    [1, 2, 4],
    [3, 3, 3],
    [1, 2, 3],
    [4, 3, 2],
    [1, 2, 0]
]

print(test(li))
