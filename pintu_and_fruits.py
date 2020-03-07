t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    z=[]
    for i in range(len(a)):
        x=a[i]
        if(x==0):
            continue
        c=0
        for j in range(i,len(a)):
            if(a[j]==x):
                c=c+b[j]
                a[j]=0
        z.append(c)
    print(min(z))
    

