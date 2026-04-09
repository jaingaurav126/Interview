class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

Line 1: Class
class ListNode:

You are defining a blueprint

Line 2: Constructor
def __init__(self, val):
    a = ListNode(10)

Python internally does:

ListNode.__init__(a, 10)

So:

self = a
val = 10

Line 3:

self.val = val
Means:

“Store this value inside this object”

So:

a.val = 10
Line 4:
self.next = None

Means:

a.next = None
