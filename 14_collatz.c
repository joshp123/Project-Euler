#include <stdio.h>
// using allman braces style, get fucked K&R


long long collatz(long long n)
{
    if (n % 2 == 0)
    {
        return n / 2.0;
    }
    else
    {
        return (3*n) + 1;
    }
}

long long doCollatz(long long start)
{
    long long last = 0;
    last = collatz(start);
    // printf("%d, %d, ", start, last);
    long long count = 2;
    while (last != 1)
    {
        last = collatz(last);
        count++;
        // printf("%d, ", last);
    }
    // printf("\n");
    return count;
}

int main()
{
    long long maxLength = 0;
    long long longestStartingNumber;
    long long start = 999999; // 1m - 1
    while (start > 0)
    {
       long long length = doCollatz(start);
       if (length > maxLength)
        {
            maxLength = length;
            longestStartingNumber = start;
            printf("Start: %d , Length %d \n", start, length);
        }
        start--; // lol
    }
    printf("Start: %d , Length %d \n", longestStartingNumber, maxLength);
    return 0;
}

