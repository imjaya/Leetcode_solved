from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        lookup = defaultdict(list)
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                invalid.add(i)
            for other_i, previous_time, other_amount, other_city in lookup[name]:
                if abs(time - previous_time) <= 60 and other_city != city:
                    invalid.add(i)
                    invalid.add(other_i)
            lookup[name].append((i, time, amount, city))
        return [transactions[i] for i in invalid]