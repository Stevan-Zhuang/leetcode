from heapq import heappop, heappush

class Node:
    def __init__(self, v, index):
        self.v = v
        self.index = index
        self.prev = None
        self.next = None

    def __lt__(self, other):
        return self.index < other.index

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        nodes = []
        for i in range(n):
            nodes.append(Node(nums[i], i))
            if i > 0:
                nodes[i - 1].next = nodes[i]
                nodes[i].prev = nodes[i - 1]

        pair_sums = []
        pairs_unsorted = 0
        for i in range(n - 1):
            heappush(pair_sums, (nums[i] + nums[i + 1], nodes[i], nodes[i + 1]))
            if nums[i] > nums[i + 1]:
                pairs_unsorted += 1
        del nodes

        count = 0
        dirty = set()
        while pairs_unsorted:
            min_pair_sum, node, node_next = heappop(pair_sums)
            if (node, node_next) in dirty:
                dirty.remove((node, node_next))
                continue

            pairs_unsorted -= node.v > node.next.v
            if node.prev is not None:
                dirty.add((node.prev, node))
                pairs_unsorted -= node.prev.v > node.v
            if node.next.next is not None:
                dirty.add((node.next, node.next.next))
                pairs_unsorted -= node.next.v > node.next.next.v

            new_node = Node(min_pair_sum, node.index)
            if node.prev is not None:
                node.prev.next = new_node
                new_node.prev = node.prev
            if node.next.next is not None:
                node.next.next.prev = new_node
                new_node.next = node.next.next

            if node.prev is not None:
                pairs_unsorted += (node.prev.v > new_node.v)
                heappush(pair_sums, (node.prev.v + new_node.v, node.prev, new_node))
            if node.next.next is not None:
                pairs_unsorted += (new_node.v > node.next.next.v)
                heappush(pair_sums, (new_node.v + node.next.next.v, new_node, node.next.next))

            count += 1
        return count
