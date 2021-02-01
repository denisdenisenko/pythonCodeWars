def next_bigger(n):
    s = list(str(n))
    i = j = 0
    length = len(s)-1
    while i < length and s[i + 1] <= s[i]: i -= 1
    if i >= length: return -1
    while s[j] >= s[i + 1]: j += 1
    s[i], s[j+1] = s[j+1], s[i]
    s[:i] = reversed(s[:i])
    if s[length] == '0': return -1
    print(int(''.join(s)))
    return int(''.join(s))

next_bigger(12)