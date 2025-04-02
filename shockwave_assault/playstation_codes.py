from itertools import count, product

TARGETS = {
    0x000a738a: None,
    0x00008400: None,
    0x00008840: None,
    0x00008c40: None,
    0x0000c600: None,
    0x009c771c: None,
    0x0037d2b7: None,
    0x3aa2abe2: None,
    0x9210cc50: None,
    0x0000fbc0: None,
    0x00a2a1a2: None,
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
        if button == 'X':
            ret = ret * 4 + 1
        elif button == 'Square':
            ret = ret * 4 + 2
        elif button == 'Circle':
            ret = ret * 4 + 3
        elif button == 'Triangle':
            ret = ret << 2
    
    return ret


def get_button_sequences():
    found = 0
    for i in count(1):
        for seq in product(['X', 'Square', 'Circle', 'Triangle'], repeat=i):
            x = combine_buttons(seq)
            y = transform(x)
            if y in TARGETS and TARGETS[y] is None:
                TARGETS[y] = seq
                found += 1
                print(found, ', '.join(seq), sep='. ')
                if found == len(TARGETS):
                    return


if __name__ == '__main__':
    get_button_sequences()
