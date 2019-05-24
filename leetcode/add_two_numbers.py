#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    t_b = 0
    prev_node = None
    ll = []
    while l1 or l2:
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)
        if t_b > 0:
            t_v = t_b + l1.val + l2.val
            t_b = 0
        else:
            t_v = l1.val + l2.val
        if t_v >= 10:
            t_b = t_b + 1
            t_v = t_v - 10
        if prev_node is not None:
            prev_node.next = ListNode(t_v)
        else:
            prev_node = ListNode(t_v)
        l1 = l1.next
        l2 = l2.next
        ll.append(prev_node.val)
        prev_node = prev_node.next
    if t_b > 0:
        ll.append(ListNode(t_b).val)
    return ll

def main():
    a, b, c = ListNode(1), ListNode(2), ListNode(3)
    d, e, f = ListNode(9), ListNode(8), ListNode(7)
    a.next = b
    b.next = c
    d.next = e
    e.next = f
    print(addTwoNumbers(a, d))


if __name__ == '__main__':
    main()