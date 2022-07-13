from statistics import median
for i in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    j = -1
    while m>1:
    
        ans+=a[j]
        m-=1
        j-=1
    
    if j==-1:
        j = n-1
    ans = median(a[:j+1])

    print(f'Case #{i+1} {ans}')