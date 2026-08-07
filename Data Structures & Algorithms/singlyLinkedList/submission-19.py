class Node:
    def __init__(self, val: int, next: "Node | None" = None):
        self.value = val
        self.next = next

class LinkedList:
    def __init__(self):
        # We only need the head pointer to track the list
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr is not None:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1  # Index out of bounds

    def insertHead(self, val: int) -> None:
        # Create a new node pointing to the current head, then update head
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        
        # Base case: Empty list
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node (the tail)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        # Special case: Removing the head node (index 0 has no predecessor inside the list)
        if index == 0:
            self.head = self.head.next
            return True

        # Traverse to the PREDECESSOR node (index - 1)
        curr = self.head
        i = 0
        while curr is not None and i < index - 1:
            curr = curr.next
            i += 1

        # If index is out of bounds or there is no target node      at 'index'
        if curr is None or curr.next is None:
            return False

        # Bypass the node at 'index'
        curr.next = curr.next.next
        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.value)
            curr = curr.next
        return values