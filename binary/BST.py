'''
Name: Alexis Gray
Purpose: Binary Search Tree Class
'''

from bNode import bNode
from pokemon import Poke

class BST: 

    def __init__(self):
        self._root = None 

    def search(self, key):  
        return self._recSearch(key, self._root)

    def _recSearch(self, key, curNode):
        if curNode == None:
            raise IndexError("Not in tree!")

        if curNode.entry == key:
             return curNode.entry

        if curNode.entry < key:
            return self._recSearch(key, curNode.right)
        if curNode.entry > key: 
            return self._recSearch(key, curNode.left)
        else:
            raise RuntimeError("Not in tree!")

    def add(self, entry):  
        if self._root == None:
            self._root = bNode(entry)
       
        elif self._root.entry < entry:
            if self._root.right == None:
                self._root.right = bNode(entry)
            else:
                self._recAdd(entry, self._root.right)

        elif self._root.entry > entry:
            if self._root.left == None:
                self._root.left = bNode(entry)
            else:     
                self._recAdd(entry, self._root.left)

        else:
            raise RuntimeError("No Duplicates! ")

    def _recAdd(self, entry, curNode):
        if curNode.entry < entry:
            if curNode.right == None:
                curNode.right = bNode(entry)
            else:
                self._recAdd(entry, curNode.right)

        elif curNode.entry > entry:
            if curNode.left == None: 
                curNode.left = bNode(entry)

            else:
                self._recAdd(entry, curNode.left)

        else:
            raise RuntimeError("No Duplicates!")

    def remove(self, key):
        if self._root == None: 
            raise RuntimeError("Empty Tree!")
        else:
            self._recRemove(key, self._root)

    def _recRemove(self, key,  curNode):
        if curNode.entry > key: 
            curNode.left = self._recRemove(key, curNode.left)

        elif curNode.entry < key: 
            curNode.right = self._recRemove(key, curNode.right)

        else: 
            if curNode.left == None and curNode.right == None:
                curNode = None
                return None

            elif curNode.left == None:
                temp = curNode.right
                curNode = None
                return temp


            elif curNode.right == None:
                temp = curNode.left
                curNode = None 
                return temp
                

            else:
                temp = self.greatestofST(curNode.left)
                curNode.entry = temp.entry
                self._recRemove(temp.entry.ID, curNode.left)

        return curNode



    def preOrder(self, visit):  
        if self._root != None:
            self._recPreOrder(visit, self._root)

    def _recPreOrder(self, visit, curNode):
        visit(curNode.entry)

        if curNode.left != None:
            self._recPreOrder(visit, curNode.left)

        if curNode.right != None:
            self._recPreOrder(visit, curNode.right)


    def inOrder(self, visit):  
        if self._root != None:
            self._recInOrder(visit, self._root)

    def _recInOrder(self, visit, curNode):
        if curNode.left != None: 
            self._recInOrder(visit, curNode.left)

        visit(curNode.entry)

        if curNode.right != None:
            self._recInOrder(visit, curNode.right)


    def postOrder(self, visit):  
        if self._root != None:
            self._recPostOrder(visit, self._root)

    def _recPostOrder(self, visit, curNode):
        if curNode.left!= None:
            self._recPostOrder(visit, curNode.left)

        if curNode.right!= None:
            self._recPostOrder(visit, curNode.right)

        visit(curNode.entry)

    
    def greatestofST(self, curNode):
        if curNode.right == None:
            return curNode

        else:
            return self.greatestofST(curNode.right)

    
   

    



        


        



