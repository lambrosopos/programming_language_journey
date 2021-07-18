# efinition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_num(listnode):
            curr_node = listnode
            num = str(curr_node.val)
            while (curr_node.next):
                curr_node = curr_node.next
                num = str(curr_node.val) + num

            return int(num)

        num_1 = get_num(l1)
        num_2 = get_num(l2)

        sum_num = str(num_1 + num_2)
        
        last_node = ListNode(int(sum_num[0]))
        
        if len(sum_num) == 1:
            return last_node
            
        for s in sum_num[1:]:
            if s == "0":
                s = 0
            new_node = ListNode(int(s), last_node)
            last_node = new_node
            
        return new_nodeD
