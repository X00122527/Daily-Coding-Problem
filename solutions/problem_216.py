def roman(arr):
 
    romans = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }
    arr = list(reversed(arr))
    prev = arr[0] 
    total = romans[prev]
    for i in range(1, len(arr)):

        if romans[prev] <= romans[arr[i]]:
            total += romans[arr[i]]
        else:
            total -= romans[arr[i]]
        prev = arr[i]
    return total
 
if __name__ == '__main__':
    assert roman('MDCCI') == 1701
    assert roman('IV') == 4
    assert roman('IX') == 9
    assert roman('XIX') == 19