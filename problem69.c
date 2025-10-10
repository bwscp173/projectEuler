#include <math.h>
#include <stdio.h>
#define LIMIT 1000000

int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}


int main() {
    int *phi = malloc((LIMIT + 1) * sizeof(int));

    for (int i = 0; i <= LIMIT; i++)
        phi[i] = i;  // Initialize φ(n) = n

    // Euler's Totient sieve
    for (int i = 2; i <= LIMIT; i++) {
        if (phi[i] == i) { // i is prime
            for (int j = i; j <= LIMIT; j += i) {
                phi[j] -= phi[j] / i;
            }
        }
    }

    // Find max φ(n)
    int answer = 0;
    int number = 0;
    for (int i = 1; i <= LIMIT; i++) {
        if (phi[i] > answer) {
            answer = phi[i];
            number = i;
        }

        if (i % 100000 == 0)
            printf("%d/1000000 processed\n", i);
    }

    printf("Max φ(n) = %d (at n = %d)\n", answer, number);

    free(phi);
    getchar();
    return 0;
}