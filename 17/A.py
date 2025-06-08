#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	ll n,num;
	cin>>n>>num;
	if(num == 0){
		cout<<"YES";
		return 0;
	}
	vector<ll> a(n+1,0);
	for(int i = 2; i<n+1; i++){
		for(int j = 2*i; j < n+1; j += i){
			a[j] = 1;
		}
	}
	
	int count = 0;
	
	vector<ll> primes;
	for(int i = 2; i<n+1; i++){
		if(a[i] == 0){
			primes.push_back(i);
		}
	}
	
	for(int i = 0; i<primes.size(); i++){
		int current = primes[i]+primes[i+1]+1;
		for(int j = i + 2; j < primes.size(); j++){
			if(current == primes[j]){
				count++;
				if(count == num){
					cout<<"YES";
					return 0;
				}
			}
		}
		
	}
	cout<<"NO";
	return 0;
	
}
