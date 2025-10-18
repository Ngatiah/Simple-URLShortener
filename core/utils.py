'''
Base62 encodes random number(ID) for long url 
Best choice for short, reversible, URL-safe codes.
Works perfectly with auto-increment IDs or UUID-derived integers.
Can easily extend with analytics, expiry, or user accounts later.
'''
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode_base62(num: int) -> str:
    """Convert a positive integer to a Base62 string."""
    if num == 0:
        return ALPHABET[0]
    base62 = ""
    while num > 0:
        num, rem = divmod(num, 62)
        base62 = ALPHABET[rem] + base62
    return base62


def decode_base62(s: str) -> int:
    """Convert a Base62 string back to integer."""
    num = 0
    for char in s:
        num = num * 62 + ALPHABET.index(char)
    return num

# print(decode_base62('cd'))
