def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    res = []
    tempinter = intervals[0]
    for i in intervals[1:]:
        if tempinter[1] >= i[0]:
            if tempinter[1] >= i[1]:
                continue
            else:
                tempinter[1] = i[1]
        else:
            res.append(tempinter)
            tempinter = i
    res.append(tempinter)
    return res



