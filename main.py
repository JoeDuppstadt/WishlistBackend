def strStr(haystack, needle):
    needleIndex = 0
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[needleIndex]:
            needleIndex = needleIndex + 1
            i += 1

        else:
            i = i - needleIndex + 1
            needleIndex = 0


        if needleIndex == len(needle):
            return 1000
    return -1

print(strStr('ississippi', 'issip'))

