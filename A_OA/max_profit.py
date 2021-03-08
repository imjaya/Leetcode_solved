from collections import Counter

def supplierInventory(numSupplier, inventory, order):
    d = Counter()
    for i in range(numSupplier):
        d[inventory[i]] += 1
    
    cur = max(d)
    profit = 0
    while order > 0 and cur > 0:
        freq = d[cur]

        if order >= freq:
            order -= freq
            profit += cur * freq
        elif order < freq:
            profit += order * cur
            break
            
        cur -= 1
        d[cur] += freq
    
    return profit

print(supplierInventory(5,  [3, 5, 7, 10, 6], 20)) # 107
print(supplierInventory(2,  [3, 4], 6)) # 15