def kUniques(s, k):
    found = 0
    leng = 0
    same = 0
    for i in range(0, len(s) - 1):
        for j in range(i, len(s) - 1):
            if (s[i] == s[i + 1] and same <= k):
                print("Dc")


s = "aabacbebebe"
k = 3
kUniques(s, k)
