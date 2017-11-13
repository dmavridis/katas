# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:58:10 2016

@author: Dimitrios
"""

class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = []
        self.rightChild = []
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild      
            self.leftChild = t
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild      
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild
        
    def getRightChild(self):
        return self.rightChild
    
    def getRootVal(self):
        return self.key
        
    def setRootVal(self,obj):
        self.key = obj
        


            