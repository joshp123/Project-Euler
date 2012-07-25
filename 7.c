/*
 Euler: 7, 10001th prime
*/

#include <stdio.h>

int main() {
	int n,a,b,l,c;
	printf("For what numbers do you want to calculate primes below?\n");
	scanf("%i", &n);
	int primes[n];
	primes[1]=0; /* 1 is not prime */
	for(a=2;a<=n;a++){
		primes[a]=1;
	}
	for(a=2;a<=n;a++){
		/*printf("Running on multiples of %i \n",a);*/
		for(b=a*2;b<=n;b+=a){
			primes[b] = 0;
			/*printf("removing %i \n", b);*/
		}
	}
	printf("The prime numbers below %i are:\n", n );
	for(c=1;c<=n;c++){
	/* printf("%ith value in primes: %i \n",c, primes[c]);*/
		if(primes[c] != 0){
			printf("%i, ", c);
	}
	}
	return 0;
}