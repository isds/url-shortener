import math

from string import digits, ascii_lowercase, ascii_uppercase


def to_base_62(number, b=62):
    """
    Encode and decode to base 62.
    """
    if b <= 0 or b > 62:
        return 0
    base = digits + ascii_lowercase + ascii_uppercase
    r = number % b
    q = math.floor(number / b)
    
    result = base[r]

    while q:
        r = q % b
        q = math.floor(q / b)
        result = base[int(r)] + result
    return result


def to_base_10(number, b=62):
    """
    Encode and decode to base 10.
    """
    base = digits + ascii_lowercase + ascii_uppercase
    limit = len(number)
    result = 0
    for i in range(limit):
        result = b * result + base.find(number[i])
    return result
