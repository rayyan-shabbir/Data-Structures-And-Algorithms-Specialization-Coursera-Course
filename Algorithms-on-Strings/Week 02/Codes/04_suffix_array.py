# python3
def SuffixArray(s):
    suffix = []
    for i in range(len(s)):
        # (suffix, starting position)
        suffix.append((s[i:], i))  
    suffix.sort()
    result = []
    for e in suffix:
        result.append(e[1])
    return result


if __name__ == '__main__':
    text = input()
    suffix_array = SuffixArray(text)
    for e in suffix_array:
        print(e, end=' ')