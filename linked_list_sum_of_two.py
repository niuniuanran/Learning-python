# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':

        str1 = ''
        str2 = ''

        while l1 is not None:
            str1 = str(l1.val) + str1
            l1 = l1.next

        while l2 is not None:
            str2 = str(l2.val) + str2
            l2 = l2.next

        sum_num = int(str1) + int(str2)
        print(sum_num)
        s = ListNode(sum_num % 10)
        current = s

        while sum_num >= 10:
            sum_num = sum_num // 10
            digit = sum_num % 10
            # print(digit)
            current.next = ListNode(digit)
            current = current.next

        while s is not None:
            print(s.val)
            s = s.next

        return s


def test():
    l1 = ListNode(x=1)
    l1.next = ListNode(x=8)
    # l1.next.next = ListNode(x=3)

    l2 = ListNode(x=0)
    # l2.next = ListNode(x=6)
    # l2.next.next = ListNode(x=4)

    s = Solution()
    s.addTwoNumbers(l1, l2)


if __name__ == '__main__':
    test()


