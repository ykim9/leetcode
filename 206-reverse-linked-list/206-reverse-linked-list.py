# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None           # 반전된 linked_list
        while head:
            nxt = head.next  # 다음 노드
            head.next = cur  # 현재 노드에 반전된 linked_list 붙이기
            cur = head       # 반전된 노드: 현재 진행 상황 설정
            head = nxt       # 현재 노드: 다음에 진행할 노드로 설정
        return cur