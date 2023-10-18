'''
You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of product name and its traded volume of stocks. 
Eg: {name: vodafone, volume: 20}

What's the most efficient solution in case of:
1) You have to tell top k products traded by volume at end of day.
2) You have to tell top k products traded by volume throughout the day.

e.g. A heap to store stock by decreasing volume (updating - O(logn)and getTop k - O(k)) and a map to track stock volume (updating - O(1))

What you're looking for is a kind of map or dictionary which supports the following queries:

Add(key, x): add x to the total for that key, creating a new entry if it doesn't already exist.
GetKLargest(k): return the keys/totals for the k largest entries.
Let's say Q is the number of queries, and n is the number of distinct keys. We should assume that Q is much larger than n; choosing the NYSE as an example, there are a few thousand stocks traded, and a few million trades per day.

In the first scenario we assume that there are a large number of Add queries followed by one GetKLargest query. Since the cost of the Add query dominates, we can use a hashtable so that Add takes O(1) time, and then at the end of the day we can do GetKLargest in O(n log k) time using a priority queue of size k; note that we don't need to sort the whole key-set in O(n log n) time just to find the k largest elements. The total cost of answering Q queries is O(Q + n log k).

In the second scenario, we assume there could be a large number of both kinds of query. The cost of either query could dominate. A good option is to use an order statistic tree, which supports Add in O(log n) time, and GetKLargest in O(k log n) time. To look up a company by name in the tree requires a separate index, which can be maintained as a hashtable. The total cost is O(Qk log n) in the worst case.

If k is fixed or has a fixed limit, we can do better: keep the totals in a hashtable, but also maintain a priority queue of the current top k elements alongside. The cost of the Add query is now O(log k) because of maintaining the priority queue; to do this efficiently we need the map to also store the current index of each company in the priority queue, if it's there, otherwise searching the priority queue for the right company is O(k). The cost of GetKLargest is O(k) since we just output the contents of the priority queue. (The problem doesn't say we need to output them in order. If we do, then we can use a sorted array instead of a heap for the priority queue, and Add takes O(k) time.)

In this case, the total cost of answering Q queries is O(Qk). Note that this only works if we know in advance the maximum value of k that could be queried, before the query arrives; otherwise we don't know how big to make the priority queue.

Replies:
For the second scenario when k is variable - how is using an order statistic tree better than using a max-heap when both take O(logn) for updates? – 

A max heap cannot be used as a map/dictionary. You cannot look up a company by name in O(log n) time. You also cannot poll the largest k entries from a heap in only O(k) time. – 

It seems to me that in both second and third cases we can use ordinary binary search tree to store (aggregated volume, name) pairs. In Add operation we lookup current aggregated volume in hashtable, remove corresponding pair from a BST, insert a new pair back with updated volume in O(log(size(BST)) and update aggregated volume in hashtable. In GetKLargest we traverse k elements of BST in-order in O(k). – 

looking back now, there is no need for an order statistic tree (though it is just a BST where each node also knows its subtree's cardinality, so it doesn't cost anything asymptotically to use one instead of a BST). You can get the k largest elements from any balanced BST by in-order traversal. That said, it's not O(k) time to do this, because e.g. in the case k=1 you can't get the smallest element (which in general could be a leaf) without descending the whole tree in O(log n) time. It might be O(k + log n) instead of O(k log n), but I can't find a source to confirm. – 
'''

import typing
from dataclasses import dataclass
from collections import defaultdict
from sortedcontainers import SortedDict


@dataclass 
class Tick:
    name: str
    qty: int

@dataclass
class StockTicker:
    accum: typing.DefaultDict[str, int]
    top: SortedDict

    def add_tick(self, tick: Tick):
        self.accum[tick.name] += tick.qty
        if tick.name not in self.accum:
            self.accum[-tick.qty] = []
        
    

    def top_k(self, k: int) -> typing.List[Tick]:
        pass

