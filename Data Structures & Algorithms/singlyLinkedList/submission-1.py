class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # A dummy node helps handle edge cases like inserting/removing at the head
        self.dummy = ListNode()
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        curr = self.dummy.next
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        
        # If the list was empty, the new head is also the tail
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.dummy
        i = 0
        
        # Traverse until we reach the node right BEFORE the target index
        while curr and i < index:
            curr = curr.next
            i += 1
            
        if curr and curr.next:
            # If the node to be removed is the tail, update the tail pointer
            if curr.next == self.tail:
                self.tail = curr
            
            curr.next = curr.next.next
            return True
            
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.dummy.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res