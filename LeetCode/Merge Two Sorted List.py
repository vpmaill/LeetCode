class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: object, list2: object) -> object:
    def fillListNode(listToFill):
        if len(listToFill) == 1:
            return ListNode(listToFill[0])
        else:
            return ListNode(listToFill[0], fillListNode(listToFill[1:]))
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    templist = []
    i = list1
    while i != None:
        templist.append(i.val)
        i = i.next
    i = list2
    while i != None:
        templist.append(i.val)
        i = i.next
    templist = sorted(templist)
    if not templist:
        return None
    return fillListNode(templist)


def ListNodeToPrint(s):
    res = []
    while s != None:
        res.append(s.val)
        s = s.next
    return res


l1 = ListNode(1)
a = mergeTwoLists(l1, l1)
print(ListNodeToPrint(a))
