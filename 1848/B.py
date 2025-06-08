#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	ll n;
	cin>>n;
	
	vector<ll> a(n+2,1);
	int add = 0;
	for(int i = 2; i<= n+1;i++){
		for(int j = 2*i; j < n+2; j+=i){
			a[j]= 2;
			add++;
		}
	}
	if(add>0){
		cout<<2<<"\n";
	}
	else cout<<1<<"\n";
	
	for(int i = 2; i<= n+1 ; i++){
		cout<<a[i]<<" ";
	}
	
	return 0;
}
