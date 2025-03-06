class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll=ListNode()
        cur=ll
        carry=0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            val=n1+n2+carry
            carry=val//10
            val=val%10
            cur.next=ListNode(val)
            
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return ll.next