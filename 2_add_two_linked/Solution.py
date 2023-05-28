from typing import Optional


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_ = self.getNum(l1) + self.getNum(l2)
        return self.toNodeList(result_)

    def getNum(self, l_list: Optional[ListNode]) -> int:
        sum_ = []

        curr_ = l_list
        while True:
            if curr_ == None:
                break
            print(curr_.val)
            sum_.append(curr_.val)
            curr_ = curr_.next

        return int("".join(str(i) for i in reversed(sum_)))

    def toNodeList(self, num_: int) -> Optional[ListNode]:
        list_of_nums = [int(i) for i in reversed(str(num_))]
        head = ListNode(list_of_nums[0])
        tail = head

        c = 1
        while c < len(list_of_nums):
            print(head)
            tail.next = ListNode(list_of_nums[c])
            tail = tail.next
            c += 1

        return head


l1 = ListNode(0)
l2 = ListNode(0)

print(Solution().addTwoNumbers(l1, l2).val)
