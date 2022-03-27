# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(None, head)
        prev = dummy
        while head:              # 다음 노드가 없으면 중단
            if head.val == val:  # 값을 삭제해야할 경우
                prev.next = head.next # 이전 노드에 현재 노드 다음 노드를 연결
            else:               
                prev = head
            head = head.next

        return dummy.next
