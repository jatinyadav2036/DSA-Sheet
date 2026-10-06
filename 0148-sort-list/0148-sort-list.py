class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Base case
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        right = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # Attach remaining nodes
        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next
