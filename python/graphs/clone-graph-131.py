"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        createdNodes = {}

        def createNode(cnode: Optional["Node"], createdNodes={}):
            neighlist = []
            if createdNodes.get(cnode.val) is None:
                newNode = Node(cnode.val)
                createdNodes[cnode.val] = newNode
                for neighbour in cnode.neighbors:
                    neighlist.append(createNode(neighbour, createdNodes))
                newNode.neighbors = neighlist
                createdNodes[cnode.val].neighbors = neighlist
            else:
                newNode = createdNodes.get(cnode.val)
            return newNode

        if not node:
            return
        else:
            return createNode(node, createdNodes)
