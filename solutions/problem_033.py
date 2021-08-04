def getMedian(seq):
    if(seq == 0):
        return False
    seq = sorted(seq)
    if(len(seq) % 2 == 0):
        return (seq[len(seq)//2-1] + seq[len(seq)//2]) / 2
    else:
        return seq[len(seq) // 2]


def generateSingleMedian(median):
    medians = []
    for i in range(0, len(median)):
       medians.append(getMedian(median[:i+1]))

    return medians

if __name__ == '__main__':
    assert generateSingleMedian([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
    assert not generateSingleMedian([])
    #
    # assert getMedian([3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29]) == 22.0
    # assert getMedian([3, 6, 5, 9]) == 5.5
    # assert getMedian([3, 6, 5, 9, 12, 10, 7, 2, 2]) == 6
    # assert getMedian([3, 6, 5, 10, 4, 9, 12, 10, 7, 2, 2]) == 6
    # assert getMedian([3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]) == 23

