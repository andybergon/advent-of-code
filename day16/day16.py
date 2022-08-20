def load(filename):
    with open(filename) as f:
        return f.readline().strip()


def sum_version_numbers(binary):
    version = binary[:3]
    type = binary[3:6]
    if int(type, 2) == 4:  # literal
        value, rest = get_literal_value(binary)
    else:  # operator
        length_type = binary[6]
        if length_type == '0':
            # 15 bits -> bit length of sub-packets
            bit_length = binary[7:7 + 15]
            return version + sum_version_numbers()
        else:
            num_subpackets = binary[7:7 + 11]
            # 11 bits -> number of sub-packets
            pass
    return version_sum


def get_literal_value(binary):
    rest = binary[6:]
    value = ''
    while rest and len(rest) >= 5:
        bin_value = rest[1:5]
        value += bin_value
        rest = rest[5:]
        if rest[0] == '0':
            break
    return int(value, 2), rest


def part_one(filename):
    s = load(filename)
    binary = bin(int(s, 16))[2:]
    vs = sum_version_numbers(binary)
    print(vs)


def part_two(filename):
    m = load(filename)
    print(m)


if __name__ == '__main__':
    part_one('day16test.txt')  # ? # ? min
    # part_two('day16test.txt')  # ? # ? min
