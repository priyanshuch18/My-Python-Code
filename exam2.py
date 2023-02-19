def removekth(s,k):
    for i in range(len(s)):
        if i!=k:
            s+=s[i]
        return s
print(removekth("python",2))