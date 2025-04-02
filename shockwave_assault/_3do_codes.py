from itertools import count, product

TARGETS = {
    0x00008c40: None,
    0x00290c69: None,
    0x00a77b67: None,
    0x00f37373: None,
    0x00fb9c3b: None,
    0x1CAC986C: None,
    0x2723C523: None,
    0x0029b9e9: None,
    0x9916EE56: None,
}

def transform(x):
    for i in range(10):
        x = x << 1 ^ (x << 1 & 0x4000) >> 3
        x = x ^ (x & 0x800) >> 5
        x = x ^ (x & 0x20000) >> 2
        x = x ^ (x & 0x10000) >> 0x10

    return x


def combine_buttons(seq):
    ret = 0
    for button in seq:
        if button == 'A':
            ret = ret * 4 + 1
        elif button == 'B':
            ret = ret * 4 + 2
        elif button == 'C':
            ret = ret * 4 + 3
    
    return ret


def get_button_sequences():
    found = 0
    for i in count(1):
        for seq in product(['A', 'B', 'C'], repeat=i):
            x = combine_buttons(seq)
            y = transform(x)
            if y in TARGETS and TARGETS[y] is None:
                TARGETS[y] = seq
                found += 1
                print(found, ''.join(seq) + 'X', sep='. ')
                if found == len(TARGETS):
                    return

if __name__ == '__main__':
    get_button_sequences()
