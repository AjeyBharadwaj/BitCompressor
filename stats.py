import math

def calc(file_name):
    total = count = 0
    with open(file_name, 'r') as fp:
        data = fp.read()
        hit = [0]*8
        miss = [0]*8
        bits = [1, 2, 4, 8, 16, 32, 64, 128]
        prev = ord(data[0])
        for c in data:
            count += 1

            cur = ord(c)
            for i in range(0, len(bits)):
                if abs(cur-prev) < bits[i]:
                    hit[i] += 1
                else:
                    miss[i] += 1

            total += abs(cur-prev)
            prev = cur
    return total, count, hit, miss


#total, count, hit, miss = calc("IMDB-Dataset.csv")

total, count, hit, miss = (2131996362, 66200352, [1373129, 4838092, 11166499, 19692049, 36453408, 41838578, 44981447, 66191970], [64827223, 61362260, 55033853, 46508303, 29746944, 24361774, 21218905, 8382])



savings = ((8-2-int(math.log2(total/count)))*total)/8

print(f"Size : {count}")
for i in range(0, len(hit)):
    op_bits = 2
    bits_per_entry = op_bits+i
    total_bits = (bits_per_entry*hit[i])+((8+op_bits)*miss[i])
    total_bytes = total_bits/8

    if total_bytes<count:
        print(f"With {i} bits difference, we can save : {count-total_bytes} bytes")


pass