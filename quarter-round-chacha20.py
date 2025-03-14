def to_binary_string(value):
    """Convert an integer to a 32-bit binary string."""
    return format(value & 0xFFFFFFFF, '032b')

def quarter_round(a, b, c, d):
    """Perform a quarter round on four 32-bit integers with verbose output."""
    print(f"Initial values: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 1: a += b
    a += b
    print(f"After a += b: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 2: d ^= a
    d ^= a
    print(f"After d ^= a: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 3: d <<<= 16 (rotate left by 16)
    d = (d << 16) | (d >> (32 - 16))
    print(f"After d <<<= 16: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 4: c += d
    c += d
    print(f"After c += d: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 5: b ^= c
    b ^= c
    print(f"After b ^= c: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 6: b <<<= 12 (rotate left by 12)
    b = (b << 12) | (b >> (32 - 12))
    print(f"After b <<<= 12: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 7: a += b
    a += b
    print(f"After a += b: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 8: d ^= a
    d ^= a
    print(f"After d ^= a: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 9: d <<<= 8 (rotate left by 8)
    d = (d << 8) | (d >> (32 - 8))
    print(f"After d <<<= 8: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 10: c += d
    c += d
    print(f"After c += d: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 11: b ^= c
    b ^= c
    print(f"After b ^= c: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    # Step 12: b <<<= 7 (rotate left by 7)
    b = (b << 7) | (b >> (32 - 7))
    print(f"After b <<<= 7: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")

    return a, b, c, d

# Example usage
if __name__ == "__main__":
    # Example input values (32-bit integers)
    a = 0x1  # 00000000000000000000000000000001
    b = 0x2  # 00000000000000000000000000000010
    c = 0x3  # 00000000000000000000000000000011
    d = 0x4  # 00000000000000000000000000000100

    print(f"Input: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")
    a, b, c, d = quarter_round(a, b, c, d)
    print(f"Output: a={a}, b={b}, c={c}, d={d}\n")