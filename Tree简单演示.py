class TreeNode:
    def __init__(self,x):
        self._val=x
        self.left=None
        self.right=None


treenode_A=TreeNode('A')#每一个节点
treenode_B=TreeNode('B')#
treenode_C=TreeNode('C')
treenode_D=TreeNode('D')
treenode_E=TreeNode('E')
treenode_F=TreeNode('F')

treenode_A.left=treenode_B
treenode_A.right=treenode_C
treenode_B.left=treenode_D
treenode_B.right=treenode_E
treenode_C.right=treenode_F

