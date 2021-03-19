from heapq import heapify, heappop, heappush
# from typing import List

def fiveStartReviews(productRatings, ratingsThreshold):
    heap = []
    total_percent = 0
    for rating, total in productRatings:
        percent = rating / total * 100
        new_percent = (rating + 1) / (total + 1) * 100
        increase = new_percent - percent
        heapq.heappush(heap, (-increase, rating, total))
        total_percent += percent
    
    n = len(productRatings)
    ans = 0
    while (total_percent / n < ratingsThreshold):
        increase, rating, total = heapq.heappop(heap)
        
        total_percent = total_percent + abs(increase)
        ans += 1
        
        rating += 1
        total += 1
        percent = rating / total * 100
        next_percent = (rating + 1) / (total + 1) * 100
        increase = next_percent - percent
        heapq.heappush(heap, (-increase, rating, total))

    return ans
                    