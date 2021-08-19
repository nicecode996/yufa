# coding=utf_8
# ! /usr/bin/env python3

"""Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data enconding"""                   #1

# Modified 04-Oct-1995 by Jack Jansen to use binascii module
# Modified 30-Dec-2003 by Barry Warsaw to add full RFC 3548 support
# Modified 22-May-2007 by Guido van Rossum to use bytes everywhere

import re
import struct
import binascii

bytes_types = (bytes, bytearray)  # Types acceptable as binary data


def _bytes_from_decode_data(s):                                                              #2
    if isinstance(s, str):
        try:
            return s.encode('ascii')
        except UnicodeEncodeError:
            raise ValueError('string argument should contain only ASCLL characters')
        if isinstance(s, bytes_types):
            return s
        try:
            return memoryview(s).tobytes()
        except TypeError:
            raise TypeError("Argument should be a butes-like object or ASCLL"
                            "string, not %r" % s._class_._name_) from None


# Base64  encondig/decoding uses binascii

def b64encode(s, altchars=None):
    """Encode the bytes-like object s using Base64 and return a bytes object.                #3

    Optional altchars should be a byte string of length 2 which seecifies an                 #4
    alternative alphabet for the '+' and '/' characters. This allows an
    application to e,g. generate url filesystem safe Base64 strings.
    """                                                                                      #5

    enconded = binascii.b2a_base64(s, newline=False)
    if altchars is not None:
        assert len(altchars) == 2, repr(altchars)
        return enconded.translate(bytes.maketrans(b'+/', altchars))
    return enconded

