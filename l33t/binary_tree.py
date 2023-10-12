import typing


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(nums: typing.Sequence[typing.Optional[int]], depth: int = 0, offset: int = 0) -> typing.Optional[TreeNode]:
    print(f'offset is {offset} for depth {depth} and offset {offset}')
    if len(nums) == 0 or nums[offset] is None:
        return None
    print(f'val {nums[offset]} jump {depth + 2 ** depth}')
    return TreeNode(
        val = nums[offset],
        left  = create_tree(nums[2 ** depth:], depth+1, offset * 2), 
        right = create_tree(nums[2 ** depth:], depth+1, offset * 2 + 1))

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


