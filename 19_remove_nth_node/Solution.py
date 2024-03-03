from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ = 1
        current = head
        while current.next != None:
            len_ += 1
            current = current.next

        del_i = len_ + 1 - n
        curr_i = 1

        if del_i == curr_i:
            head = head.next
            return head

        self.delete_node_i(head, del_i)

        return head

    def delete_node_i(self, head, i):
        index = 1
        current = head
        while current.next and index < i:
            prev = current
            current = current.next
            index += 1
        if index == 0:
            head = head.next
        else:
            prev.next = current.next
