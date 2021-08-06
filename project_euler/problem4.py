"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(num, maxnum):
    """
    return should is 906609
    >>> palindrome(100, 1000)
    906609
    """
    set_palindrome = (
        i * j
        for i in range(num, maxnum)
        for j in range(num, maxnum)
        if str(i * j) == str(i * j)[::-1]
    )
    return max(set_palindrome)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
