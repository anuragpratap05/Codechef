t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    #print(s)
    y=sorted(s,reverse=True)
    sum=0
    ans=0
    #print(y)
    for i in range(n):
        x=y[i]-i
        if(x>0):
            ans=ans+x
        else:
            break
    print(ans%1000000007)
