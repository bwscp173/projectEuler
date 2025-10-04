#include <math.h>

int d(int n){
    int divisors=1;
    for (int i = 1; i < (int)(n/2)+1; i++)
    {
        if (n%i==0)
        {
            divisors++;
        }
    }
    return divisors;
}

int M(int n, int k){
    int max_divisor = 0;
    int result = 0;
    for (int j = n; j < (n+k); j++)
    {
        result = d(j);
        if (result > max_divisor){
            max_divisor = result;
        };
    }
    return max_divisor;
}

int S(u,k){
    int total = 0;
    for (int n = 1; n < (u-k+2); n++)
    {
        total += M(n,k);
        printf("total: %d/%d %d\n",n,u-k+2,total);
    }
    return total;
    
}

int main(){
    //sleep(250000);
    printf("%d\n",S(1000,10));
    printf("%d\n",S(100000000,100000));
}