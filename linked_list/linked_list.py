# Design Singly Linked List
# Design a Singly Linked List class.

# Your LinkedList class should support the following operations:

# LinkedList() will initialize an empty linked list.
# int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# void insertHead(int val) will insert a node with val at the head of the list.
# void insertTail(int val) will insert a node with val at the tail of the list.
# bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
# int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
# Example 1:

# Input: 
# ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

# Output:
# [null, null, null, true, [0, 2]]
# Example 2:

# Input:
# ["insertHead", 1, "insertHead", 2, "get", 5]

# Output:
# [null, null, -1]
# Note:

# The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.

from typing import List

class Node:
    def __init__(self, val:int, next=None):
        self.val:int = val
        self.next:Node = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
      cur = self.head
      i = 0
      while cur:
        if i == index:
          return cur.val
        cur = cur.next
        i += 1
      return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        # Zero node
        if self.head is None:
          self.head = node
          self.tail = self.head
          return
        
        # One/Many nodes
        if self.head is not None:
          node.next = self.head
          self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        # Zero node
        if not self.tail:
          self.tail = node
          self.head = self.tail
          return
        
        # One/Many node
        if self.tail:
          self.tail.next = node
          self.tail = node

    def remove(self, index: int) -> bool:
      # empty
      if not self.head:
        return False
      
      if index == 0:
        self.head = self.head.next
      else:
        i = 1
        prev = self.head
        curToDel = prev.next
        while i <= index and curToDel:
          if i == index:
            if curToDel == self.tail:
              self.tail = prev
            
            prev.next = curToDel.next
            return True
          
          prev = curToDel
          curToDel = curToDel.next
          i += 1

    def getValues(self) -> List[int]:
        cur = self.head
        lst:List[int] = []
        while cur:
          lst.append(cur.val)
          cur = cur.next
        return lst


if __name__ == "__main__":
  ll = LinkedList()
  ll.insertHead(2)
  ll.insertTail(4)
  ll.insertTail(10)
  ll.insertHead(5)
  print(ll.getValues())
  ll.remove(3)
  ll.remove(0)
  print(ll.getValues())
