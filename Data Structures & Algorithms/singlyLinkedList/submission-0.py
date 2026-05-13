class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: Optional["ListNode"] = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)  # dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while i < index and curr.next:
            curr = curr.next
            i += 1

        if curr.next is None:
            return False

        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values