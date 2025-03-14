# chacha20-quarter-round

This repository contains a Python explaination of the quarter-round function used in the ChaCha20 stream cipher. The quarter-round function is a fundamental building block of the ChaCha20 algorithm, which is widely used for secure encryption.

## Overview

The ChaCha20 algorithm is a stream cipher that operates on 64-byte blocks and consists of 20 rounds of quarter-round operations. This implementation focuses on the quarter-round function, which operates on four 32-bit words.

## Features

- **Quarter-Round Function**: Implements the quarter-round operation as defined in the ChaCha20 specification.
- **Verbose Output**: Provides detailed step-by-step output showing the internal state of the variables in both decimal and binary formats.
- **Bit Representation**: Displays the values in a 32-bit binary format for better visualization of the bit manipulation.

## Usage

To use the quarter-round function, simply run the script. The example provided in the code will demonstrate how the function operates on sample input values.

### Example

```python
if __name__ == "__main__":
    # Example input values (32-bit integers)
    a = 0x1  # 00000000000000000000000000000001
    b = 0x2  # 00000000000000000000000000000010
    c = 0x3  # 00000000000000000000000000000011
    d = 0x4  # 00000000000000000000000000000100

    print(f"Input: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")
    a, b, c, d = quarter_round(a, b, c, d)
    print(f"Output: a={to_binary_string(a)}, b={to_binary_string(b)}, c={to_binary_string(c)}, d={to_binary_string(d)}\n")
