import heapq


class Item:
    def __init__(self, name, relevance, price, sort_order, sort_parameter):
        self.name = name 
        self.relevance = relevance 
        self.price = price 
        self.sort_order = sort_order 
        self.sort_parameter = sort_parameter
    
    def __lt__(self, other):  # if ascending, maxheap # if descending, minheap
        if self.sort_parameter == 0:
            if self.sort_order == 0:
                # maintain heap size k
                return self.name > other.name 
            else: 
                return self.name < other.name 
        elif self.sort_parameter == 1: 
            if self.relevance == other.relevance: 
                if self.sort_order == 0: 
                    return self.name > other.name 
                else: 
                    return self.name < other.name 
            if self.sort_order == 0: 
                    return self.relevance > other.relevance 
            else: return self.relevance < other.relevance 
        else: 
            if self.price == other.price: 
                if self.sort_order == 0: 
                    return self.name > other.name 
                else: return self.name < other.name 
        if self.sort_order == 0: 
            return self.price > other.price 
        else: 
            return self.price < other.price 
                
def items_per_page(num_of_items, items, sort_parameter, sort_order, items_per_page, page_number):
    k = (page_number+1)*items_per_page
    heap = []
    for item in items:
    # pop off top k items and reverse list to get correct priority
        heapq.heappush(heap, Item(item[0], item[1], item[2], sort_order, sort_parameter)) 
        if len(heap) > k: 
            heapq.heappop(heap)
# pop off items from pages before the target page
    ret = [heapq.heappop(heap) for i in range(len(heap))]
    for i in range(page_number*items_per_page):
        ret.pop() 
    return [item.name for item in ret[::-1]]
            
    
print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 0, 2, 1)) 
print(items_per_pages(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 1, 2, 1)) 
print(items_per_pages(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 0, 2, 1)) 
print(items_per_pages(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 1, 2, 1)) #print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 0, 2, 1)) print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 2, 1, 2, 1)) print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 0, 2, 0)) print(items_per_page(5, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18], ['item4', 17, 20], ['item5', 17, 21]], 1, 0, 2, 1)) print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 1, 0, 2, 0)) print(items_per_page(3, [['item1', 10, 15], ['item2', 3, 4], ['item3', 17, 18]], 0, 0, 2, 0))
