#Q-2 ) Palindrome Linked List 
#Answer:-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        slow = fast = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    # print(head.next.next.val)
    
    sol = Solution()
    print(sol.isPalindrome(head))