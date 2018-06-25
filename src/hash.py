import base64
def encode(a):
    encoded_str = base64.encodestring(a)
    print encoded_str
    return encoded_str
#===============================================================================
# DECODING THE HASH
#===============================================================================
def decode(encoded_str):
    a = base64.decodestring(encoded_str)
    print a
    return a


