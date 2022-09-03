"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # constaints state that the graph could have zero nodes
        if not node:
            return None
        # using a hashTable to store the mappings from the original nodes to the new clones
        hashTable = {}
        # preforming dfs to recursively go to the nodes and map all of them together
        def dfs(node):
            # we want to make sure that we are not redo-ing mappings
            if node in hashTable:
                return hashTable[node]
            # making a copy of the node if it does not exist within the hashtable
            new = Node(node.val)
            # make a mapping from the og node and the copied node
            hashTable[node] = new
            # we want to do the same for all the node's neighbors recursively
            for i in node.neighbors:
                # append neighbors to the clone
                new.neighbors.append(dfs(i))
            return new
        # "any node that we return will be good after the entire clone has been made"
        return dfs(node)
            
