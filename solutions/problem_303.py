def solution303(time):
    hour, minute = time.split(':')
    firstPoint = int(hour) * (360 // 12) % 360
    secondPoint = int(minute) * (360 / 60)

    result = int(abs(firstPoint - secondPoint))

    return result if result <180 else 360 - result

if __name__ == '__main__':

    assert solution303('12:20') == 120
    assert solution303('12:00') == 0
    assert solution303('6:30') == 0
    assert solution303('3:46') == 174

