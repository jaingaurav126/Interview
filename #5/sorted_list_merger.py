"""Problem: Merge Two Sorted Linked Lists

👉 You are given two sorted linked lists:

List 1: 1 → 3 → 5  
List 2: 2 → 4 → 6

👉 Output:

1 → 2 → 3 → 4 → 5 → 6"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

"""We use:

dummy → starting point (important trick)
tail → builds the new list

What is Dummy Node?

👉 A fake starting node to simplify logic

dummy → ?

We build from here.

"""
def megrelists(l1,l2):
    dummy=ListNode(0)  # Dummy node to simplify logic
    tail=dummy

    while l1 and l2:
        if l1.val<l2.val:
            tail.next=l1
            l1=l1.next
            tail=tail.next
        else:
            tail.next=l2
            l2=l2.next
            tail=tail.next
        
        
    
    if l1:
        tail.next=l1        
    elif l2:
        tail.next=l2    

    return dummy.next

l1=ListNode(1)
l1.next=ListNode(3)
l1.next.next=ListNode(5)

l2=ListNode(2)
l2.next=ListNode(4) 
l2.next.next=ListNode(6)

merged_head=megrelists(l1,l2)
current=merged_head 
while current:
    print(current.val, end=' → ' if current.next else '')
    current=current.next
