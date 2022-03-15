# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        node: ListNode = head
        tail: ListNode = None
        head = tail
        while node is not None:
            flag = 0
            while node.next is not None and node.val == node.next.val:
                node = node.next
                flag = 1
            if flag == 0:
                if tail is None:
                    tail = node
                    head = tail
                else:
                    tail.next = node
                    tail = node
            node = node.next
        if tail is not None:
            tail.next = None
        return head


if __name__ == "__main__":
    m = int(input())
    head: ListNode = ListNode()
    tail: ListNode = head
    for i in range(m):
        t = int(input())
        node: ListNode = ListNode(t)
        tail.next = node
        tail = node
    so = Solution()
    ans: ListNode = so.deleteDuplicates(head.next)
    while ans is not None:
        print(ans.val)
        ans = ans.next
