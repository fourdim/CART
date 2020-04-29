class Node:
    def __init__(self, feature, value, left, right):
        self.feature = feature # Name of feature.
        self.value = value     # The value used for split.
        self.left = left       # Left branch.
        self.right = right     # Right branch.