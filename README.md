This assignment focuses on implementing recursion in Python. The tasks include creating recursive functions for computing Fibonacci numbers, finding the greatest common divisor (GCD) using Euclid’s algorithm, and comparing two strings recursively.
All functions are contained in the file:
recursion.py

Included Functions
1. fibonnaci(n)
A recursive function that returns the n-th value of the Fibonacci sequence.
Base case: n == 1 or n == 2 → returns 1
Otherwise returns: fibonnaci(n-1) + fibonnaci(n-2)

3. gcd(a, b)
A recursive implementation of Euclid’s algorithm to compute the greatest common divisor.
Base case: b == 0 → returns a
Recursive case: gcd(b, a % b)

4. compareTo(s1, s2)
A string comparison function written using recursion.
Returns:
Negative value if s1 < s2
Zero if s1 == s2
Positive value if s1 > s2
Compares character-by-character using ord() values.
