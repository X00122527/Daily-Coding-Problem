def firstNonRepeatingCharacter(string):
    if len(string) == 0:
        return '_'

    dict = {}
    for s in string:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1


    for k, v in dict.items():
        if v == 1:
            return k

    return '_'

if __name__ == '__main__':
    assert(firstNonRepeatingCharacter('aaabcccdeeef') == 'b')
    assert(firstNonRepeatingCharacter('abcbad')  == 'c')
    assert(firstNonRepeatingCharacter('abcabcabc') == '_')
    assert (firstNonRepeatingCharacter('v') == 'v')
    assert (firstNonRepeatingCharacter('') == '_')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
