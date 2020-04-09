t=int(input())
for k in range(t):
    n=int(input())
    s=[i for i in range(1,n+1)]
    if(n<=3):
        print("1")
        print(n,*[i for i in range(1,n+1)])
    else:
        if(n%2!=0):
            print(n//2)
            print(3,*[i for i in range(1,4)])
            for j in range(3,n-1,2):
                print(2,s[j],s[j+1])
        if(n%2==0):
            print(n//2)
            for i in range(0,n-1,2):
                print(2,s[i],s[i+1])
            
            
