# IS211_Assignment13 - Recursion

# ---------------------------------------------------------
# Part I: Fibonacci (recursive)
# ---------------------------------------------------------

def fibonnaci(n):
    """
    Returns the nth Fibonacci number using recursion.
    The sequence starts with:
    F1 = 1, F2 = 1, F3 = 2, F4 = 3, etc.
    """
    # Base cases
    if n == 1 or n == 2:
        return 1

    # Recursive case
    return fibonnaci(n - 1) + fibonnaci(n - 2)


# ---------------------------------------------------------
# Part II: Euclid’s GCD Algorithm (recursive)
# ---------------------------------------------------------

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b
    using Euclid's recursive algorithm.
    """
    # Base case: when b becomes zero
    if b == 0:
        return a

    # Recursive case: gcd(b, remainder)
    return gcd(b, a % b)


# ---------------------------------------------------------
# Part III: String Comparison (recursive)
# ---------------------------------------------------------

def compareTo(s1, s2):
    """
    Recursively compares two strings.
    Returns:
        - negative number if s1 < s2
        - 0 if s1 == s2
        - positive number if s1 > s2
    """
    # Base case: both strings are empty
    if s1 == "" and s2 == "":
        return 0

    # Base case: first string empty -> it's smaller
    if s1 == "" and s2 != "":
        return -1

    # Base case: second string empty -> first is larger
    if s1 != "" and s2 == "":
        return 1

    # Compare first characters
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])

    # Characters equal → recursively compare the rest
    return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    print("Fibonacci(6):", fibonnaci(6))     # Expect 8
    print("gcd(48, 18):", gcd(48, 18))       # Expect 6
    print("compareTo('apple','apricot'):", compareTo("apple","apricot"))
