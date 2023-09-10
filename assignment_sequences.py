
from typing import Union


def is_palindrome(origin: Union[str, int], /) -> bool:
    """
    Return a palindrome check result
    :param origin: value to test
    :type origin: str | int
    :return: return a palindrome check result
    :rtype: bool
    This function implements two pointers method. The left pointer is
    initialized at the beginning of an origin string, and the right one -
    at the end. The check cycle compares characters at left and right
    indexes. Once the comparison is false the function returns False.
    Once left pointer is greater or equal to the right one the function
    returns True. Punctuation, word boundaries and capitalization are
    ignored.
    Usage:
    >>> assert is_palindrome("aba") is True
    >>> assert is_palindrome("abc") is False
    >>> assert is_palindrome(12345) is False
    >>> assert is_palindrome(12321) is True
    """


def get_longest_palindrome(origin: str, /) -> str:
    """
    Return the longest palindrome substring from the given input
    :param origin:
    :type origin: str
    :return: the longest palindrome
    :rtype: str
    Usage:
    >>> assert get_longest_palindrome("0123219") == "12321"
    >>> assert get_longest_palindrome("1012210") == "012210"
    """


def are_parentheses_balanced(origin: str, /) -> bool:
    """
    Return a validation result for a given parentheses sequence
    :param origin: a parentheses sequence to validate
    :type origin: str
    :return: a validation result
    :rtype: bool
    Validation rules:
    - each opening parentheses must be closed by the same type parentheses
    - open parentheses must be closed in the correct order
    - any non-parentheses characters are to be ignored
    Usage:
    >>> assert are_parentheses_balanced("({[]})") is True
    >>> assert are_parentheses_balanced(")]}{[(") is False
    """


def get_longest_uniq_length(origin: str, /) -> int:
    """
    Return the length of the longest on sequence of unique characters
    :param origin: original sequences
    :type origin: str
    :return: the length of the longest unique characters sequence
    :rtype: int
    Usage:
    >>> assert get_longest_uniq_length("abcdefg") == 7
    >>> assert get_longest_uniq_length("racecar") == 4
    """

