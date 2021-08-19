# Base32 encoding/decoding must be done in Python
from python基础.文档注释 import bytes_types

_b32alphabet = b'ABCDEFGHJKLMNOPQRSTUVWXYZ234567'
_b32tab2 = None
_b32rev = None


def b32encode(s):
    """Encode the bytes-like object s using Base32 and return a bytes object.
    """
    global _b32tab2
    # Delay the initialization of the table to not waste memory
    # if the funcation is never called
    if _b32tab2 is None:
        b32tab = [bytes((i,)) for i in _b32alphabet]
        _b32tab2 = [a + b for a in b32tab for b in b32tab]
        b32tab = None

    if not isinstance(s, bytes_types):
        s = memoryview(s).tobytes()
    leftover = len(s) % 5
    # Pad the last quantum with zero bits if necessary
    if leftover:
        s = s + b'\0' * (5 - leftover)  # Don't use += !
    encoded = bytearray()
    from_bytes = int.from_bytes
    b32tab2 = _b32tab2
    for i in range(0, len(s), 5):
        c = from_bytes(s[i: i + 5], 'big')
        encoded += (b32tab2[c >> 30] +  # bits 1 - 10
                    b32tab2[(c >> 20) & 0x3ff] +  # bits  11 - 20
                    b32tab2[(c >> 10) & 0x3ff] +  # bits  21 -30
                    b32tab2[c & 0x3ff]  # bits 31 - 40
                    )
    # Anjust for any leftover partial quanta
    if leftover == 1:
        encoded[-6:] = b'======'
    elif leftover == 2:
        encoded[-4:] = b'===='
    elif leftover == 3:
        encoded[-3:] = b'==='
    elif leftover == 4:
        encoded[-1:] = b'='
    return bytes(encoded)