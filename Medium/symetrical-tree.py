# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def symmetricalTree(tree):
    return mirrorTrees(tree.left, tree.right)

def mirrorTrees(tree1, tree2):
    if tree1 is not None and tree2 is not None and tree1.value == tree2.value:
        return mirrorTrees(tree1.left, tree2.right) and mirrorTrees(tree1.right, tree2.left)

    # if one is None or the value is different
    return tree1 == tree2

