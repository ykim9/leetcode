# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iteration
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None           # 반전된 linked_list
        while head:
            nxt = head.next  # 다음 노드
            head.next = cur  # 현재 노드에 반전된 linked list 붙이기
            cur = head       # 반전된 노드: 현재 진행 상황 설정
            head = nxt       # 현재 노드: 다음에 진행할 노드로 설정
        return cur
    
    #recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse(node, prev=None):
            if not node:                # linked list의 마지막까지 진행한 경우 반전된 list 반환
                return prev             
            nxt = node.next             # 다음 노드
            node.next = prev            # 현재 노드의 다음에 이전 노드 설정
            return _reverse(nxt, node)  # 다음 노드에 이전 노드가 설정되도록 재귀 호출
        
        return _reverse(head)