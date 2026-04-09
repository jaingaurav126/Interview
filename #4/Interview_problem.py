"""Problem: Reverse a Linked List

👉 Given a linked list:

1 → 2 → 3 → 4 → 5

👉 Output:

1 ← 2 ← 3 ← 4 ← 5

Step-by-Step Logic

We use 3 pointers:

prev → previous node
curr → current node
next_node → next node (to not lose track)"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr

    return prev

a= ListNode(1)
b= ListNode(2)
c= ListNode(3)
a.next = b
b.next = c

new_head = reverseList(b)
# Print reversed list
curr = new_head 
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
# Output: 3 -> 2 -> 1 ->
