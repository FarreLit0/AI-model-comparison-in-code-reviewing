import heapq

def kheapsort(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr[k:]:
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)
