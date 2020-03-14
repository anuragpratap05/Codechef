#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    while(t--)
    {
    int n,q;
    cin>>n;
    cin>>q;
    int a[1000005];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int j=0;j<q;j++)
    {
        int p;
        cin>>p;
        int c=0,l=0;
        for(int i=0;i<n;i++)
        {
            int z=0;
            z=a[i]^p;
            //cout<<z<<endl;
            int k=0;
            while(z!=0)
            {
                if(z & 1)
                {
                    k++;
                }
                z=z>>1;
            }
            //cout<<k<<endl;
            if(k%2==0)
            {
                c++;
            }
            if(k%2!=0)
            {
                l++;
            }

        }
        cout<<c<<" "<< l << endl;
    
    }
    //cout<<c<<endl;
    //cout<<l<<endl;
}
}
