import typing


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(nums: typing.Sequence[typing.Optional[int]], depth: int = 0, offset: int = 0) -> typing.Optional[TreeNode]:
    if len(nums) == 0 or nums[offset] is None:
        return None
    return TreeNode(
        val = nums[offset],
        left  = create_tree(nums[2 ** depth:], depth+1, offset), 
        right = create_tree(nums[2 ** depth:], depth+1, depth + offset + 1))

def print_tree(root: typing.Optional[TreeNode], depth: int = 0):
    if root is not None:
        gap = ' ' * depth
        print(f'{gap}{root.val}')
        print_tree(root.left, depth+1)
        print_tree(root.right, depth+1)

