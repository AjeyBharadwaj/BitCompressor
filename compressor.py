import math
import random
import string

class Bit:
    def __init__(self, val):
        self.val = val


class Byte:
    def __init__(self, val):
        self.val = val

def compress_str(data, max_bits=5):
    bits = []
    
    prev = ord(data[0])

    num_bits = '0'*(8-len(bin(prev)[2:]))+bin(prev)[2:]
    for _c in num_bits:
        bits.append(Bit(int(_c)))

    for c in data:
        cur = ord(c)

        diff = prev-cur

        if abs(diff) == 0:
            bits.append(Bit(0))
            bits.append(Bit(0))

        elif abs(diff) > math.pow(2, max_bits):
            bits.append(Bit(1))
            bits.append(Bit(1))

            num_bits = '0'*(8-len(bin(cur)[2:]))+bin(cur)[2:]
            for _c in num_bits:
                bits.append(Bit(int(_c)))

        elif prev < cur:
            bits.append(Bit(0))
            bits.append(Bit(1))

            num_bits = '0'*(max_bits-len(bin(abs(diff))[2:]))+bin(abs(diff))[2:]
            for _c in num_bits:
                bits.append(Bit(int(_c)))

        elif prev > cur:
            bits.append(Bit(1))
            bits.append(Bit(0))

            num_bits = '0'*(max_bits-len(bin(abs(diff))[2:]))+bin(abs(diff))[2:]
            for _c in num_bits:
                bits.append(Bit(int(_c)))

        else:
            assert False

        prev = cur

    return bits

def compress(file_name, output_file_name, max_bits=5, max_bytes_to_process=None):
    with open(file_name, 'r') as fp:
        data = fp.read()

        if max_bytes_to_process:
            data = data[:max_bytes_to_process]
        return len(data), compress_str(data, max_bits)

def bits_to_str(bits):
    ret = ''
    for i in range(0, len(bits), 8):
        val = ''.join(str(b.val) for b in bits[i:i+8])
        ret += chr(int(val, 2))

    return ret


def way_1():
    max_bytes_to_process = 100000

    for i in range(0, 8):
        size, bits = compress("IMDB-Dataset.csv", "output.comp", max_bits=i, max_bytes_to_process=max_bytes_to_process)
        conv = bits_to_str(bits)

        further_compress = []
        for j in range(0, 5):
            new_bits = compress_str(conv, max_bits=i)
            further_compress.append(len(new_bits)//8)
            conv = bits_to_str(new_bits)
        print(f"{i} : {size} vs {len(bits)//8} vs {' vs '.join(str(c) for c in further_compress)}")

def way_2():
    max_bytes_to_process = 100000

    size, bits = compress("IMDB-Dataset.csv", "output.comp", max_bits=4, max_bytes_to_process=max_bytes_to_process)
    first_conv = bits_to_str(bits)

    conv = first_conv
    further_compress = []
    for j in range(0, 5):
        new_bits = compress_str(conv, max_bits=4)
        further_compress.append(len(new_bits)//8)
        conv = bits_to_str(new_bits)
    print(f"{size} vs {len(bits)//8} vs {' vs '.join(str(c) for c in further_compress)}")

def way_3():
    max_bytes_to_process = 100000
    max_bits = 4

    printable_chars = string.ascii_letters + string.digits + string.punctuation
    str_val = ''
    for i in range(0, max_bytes_to_process):
        str_val += random.choice(printable_chars)

    bits = compress_str(str_val, max_bits=max_bits)
    first_conv = bits_to_str(bits)

    conv = first_conv
    further_compress = []
    for j in range(0, 5):
        new_bits = compress_str(conv, max_bits=max_bits)
        further_compress.append(len(new_bits)//8)
        conv = bits_to_str(new_bits)
    print(f"{len(str_val)} vs {len(bits)//8} vs {' vs '.join(str(c) for c in further_compress)}")

way_3()

pass

