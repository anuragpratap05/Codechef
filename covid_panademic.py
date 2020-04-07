t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    lst=[]
    for i in range(n):
        if(s[i]=="1"):
            lst.append(int(i))
    #print(lst)
    x=(len(lst))
    ans="YES"
    
    for i in range(x-1) :
        y=lst[i]-lst[i+1]
        #print(y)
        if(y<= -6):
            continue
        else:
            ans="NO"
            break
    print(ans)
    
    
