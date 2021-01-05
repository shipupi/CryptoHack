std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

rot_range = ord("z") - ord("a") + 1
def rot(s, n):
    r = list()
    for i in range(len(s)):
        c = s[i]
        if (c.islower()):
            r.append(chr(((ord(c) - ord("a") + n) % rot_range) + ord("a")))
        elif(c.isupper()):
            r.append(chr(((ord(c) - ord("A") + n) % rot_range) + ord("A")))
        else:
            r.append("_")
    return ''.join(r)

def decode(s):
    l = list(s)
    return decode_list(l)

def decode_list(l):
    for i in range(0, len(l)):
        l[i] = chr(l[i])
    return ''.join(l)

def hex_to_str(hex):
    l = list()
    for i in range(0,len(hex), 2):
        l.append(int(hex[i:i+2], 16))
    return decode_list(l)

def hex_to_bytearray(hex):
    l = list()
    for i in range(0,len(hex), 2):
        l.append(int_to_byte(int(hex[i:i+2], 16)))
    return l


def int_to_byte(a):
    b = bin(a)[2:]
    bytcode = ('%08d' % int(b))
    return bytcode

def decode_b64_6bits(bits):
    o = int(bits,2)
    return(chr(o))

def base64_decode(b64_string):
    padding = b64_string.count('=')
    if(padding > 0):
        b64_string = b64_string[:-1*padding]
    print(b64_string)
    ints = [std_base64chars.index(i) for i in b64_string]
    bits = [int_to_byte(i)[2:] for i in ints]
    if(padding > 0):
        bits[-1] = bits[-1][:-padding*2]
    bits = regroup(bits,8)
    newints = [int(i,2) for i in bits]
    return decode_list(newints)

def base64_encode_hex(hex):
    bytearr = hex_to_bytearray(hex)
    return base64_encode_bytearray(bytearr)

def base64_encode_bytearray(bytearr):
    response = ''
    current = bytearr[0]
    previous = ''
    response = list()
    for byte in bytearr:
        current = byte
        a = "{}{}".format(previous, current[:6-len(previous)])
        response.append(a)
        previous = current[6-len(previous):]
        if(len(previous) == 6):
            response.append(previous)
            previous = ''
    return response

def six_digits_bits_to_char(bit_arr):
    chars = list()
    for bits in bit_arr:
        chars.append(hex(int(bits,2))[2:])
    return ''.join(chars)
            
        

def regroup(bytearr, n):
    joined = ''.join(bytearr)
    split = [joined[i:i+n] for i in range(0,len(joined), n)]
    return split

def hex_to_base64(hex):
    bytearr = hex_to_bytearray(hex)
    grouped6 = regroup(bytearr, 6)
    grouped6ints = [int(i,2) for i in grouped6]
    converted = [std_base64chars[i] for i in grouped6ints]
    return ''.join(converted)


def base16_decode(encoded):
    if (encoded[:2] == "0x"):
        encoded = encoded[2:]
    resp = ''
    s = str(encoded)
    for i in range(0,len(encoded),2):
        resp += chr(int(s[i:i+2], 16))
    return resp

def base10_decode(encoded):
    h = hex(encoded)[2:]
    return base16_decode(h)

# ex = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# ex2 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# ex3 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# ex4 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(decode_list(ex))
# print(hex_to_str(ex2))
# print(hex_to_base64(ex3))
# print(base10_decode(ex4))

a = "bXVsZV9jb25zdWx0YXRpb25zX3NraWQ="
print(base64_decode(a))
