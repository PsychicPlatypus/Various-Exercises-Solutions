class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        traversed = []
        curr = head
        while curr.next != None:
            if str(curr) in traversed:
                return True

            traversed.append(str(curr.val))
            curr = curr.next

        return False
