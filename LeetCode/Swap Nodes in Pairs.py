class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reedNode(nodeToList):
    res = []
    while nodeToList != None:
        res.append(nodeToList.val)
        nodeToList = nodeToList.next
    return res


def fillNode(listOfNums):
    if not listOfNums:
        return None
    else:
        return ListNode(listOfNums[0], fillNode(listOfNums[1:]))


def swapPairs(head):
    nums = reedNode(head)

    for i in range(1, len(nums), 2):
        nums[i - 1], nums[i] = nums[i], nums[i - 1]

    return fillNode(nums)


print(reedNode(swapPairs(fillNode([1, 2, 3, 4, 5]))))
