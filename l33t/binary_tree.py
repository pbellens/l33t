import typing


class TreeNode:
    def __init__(self, val = 0, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def create_tree(nums: typing.Sequence[typing.Optional[int]], depth: int = 0, offset: int = 0, parent: TreeNode = None) -> typing.Optional[TreeNode]:
    if len(nums) == 0 or nums[offset] is None:
        return None
    n = TreeNode(val = nums[offset], parent = parent)
    left = create_tree(nums[2 ** depth:], depth+1, offset * 2, parent = n) 
    right = create_tree(nums[2 ** depth:], depth+1, offset * 2 + 1, parent = n)
    n.left = left
    n.right = right
    return n


def print_tree(root: typing.Optional[TreeNode], depth: int = 0):
    gap = ' ' * depth
    print(f'{gap}{root.val if root else "."}')
    if root is not None and (root.left is not None or root.right is not None):
        print_tree(root.left, depth+1)
        print_tree(root.right, depth+1)

def print_tree_orig(root: typing.Optional[TreeNode], depth: int = 0):
    if root is not None:
        gap = ' ' * depth
        print(f'{gap}{root.val}')
        print_tree(root.left, depth+1)
        print_tree(root.right, depth+1)


def in_order_rec(root: typing.Optional[TreeNode]):
    if root:
        for l in in_order_rec(root.left):
            yield l
        yield root
        for r in in_order_rec(root.right):
            yield r

def in_order_it(root: typing.Optional[TreeNode]):
    to_visit = []
    current = root
    while True:
        if current:
            to_visit.append(current)
            current = current.left
        elif to_visit:
            current = to_visit.pop()
            yield current
            current = current.right
        else:
            break








