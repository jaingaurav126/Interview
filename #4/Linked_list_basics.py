"""What is a Linked List?

A Linked List is a chain of nodes:
[1 | • ] → [2 | • ] → [3 | • ] → [4 | None]

Each node has:

value (data)
pointer (next) → tells where the next node is

Build Your First Node"""
class ListNode:
    def __init__(self, val):
        self.val = val      # data
        self.next = None    # pointer
        

"""Create a Linked List Manually"""

a = ListNode(1) #a.val = 1 a.next = None
b = ListNode(2) #b.val = 2 b.next = None
c = ListNode(3) #c.val = 3 c.next = None

a.next = b
b.next = c

"""How to Traverse (VERY IMPORTANT)"""

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

print_list(a)  # Output: 1 -> 2 -> 3 ->