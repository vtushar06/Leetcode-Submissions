class RangeFreqQuery(object):

    def __init__(self, arr):
        self.index_map = {}
        for i, num in enumerate(arr):
            if num not in self.index_map:
                self.index_map[num] = []
            self.index_map[num].append(i)

    def query(self, left, right, value):
        if value not in self.index_map:
            return 0
        
        indices = self.index_map[value]
        return self.count_in_range(indices, left, right)

    def count_in_range(self, indices, left, right):
        # Binary search for lower bound
        low, high = 0, len(indices) - 1
        while low <= high:
            mid = (low + high) // 2
            if indices[mid] >= left:
                high = mid - 1
            else:
                low = mid + 1
        lb = low

        # Binary search for upper bound
        low, high = 0, len(indices) - 1
        while low <= high:
            mid = (low + high) // 2
            if indices[mid] > right:
                high = mid - 1
            else:
                low = mid + 1
        ub = low

        return max(ub - lb, 0)