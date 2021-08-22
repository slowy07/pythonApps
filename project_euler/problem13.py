"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import os


def answr():
    """
    Returns the first ten digits of the sum of the array elements
    from the file problem13.txt
    >>> answr()
    '5537376230'
    """
    file_path = os.path.join(os.path.dirname(__file__), "problem13.txt")
    with open(file_path) as file:
        return str(sum([int(line) for line in file]))[:10]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
