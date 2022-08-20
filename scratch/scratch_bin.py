if __name__ == '__main__':
    b = bin(int("1BD4", 16))[2:]
    print(b.zfill(8))

    bin_a = bin(42)  # int => 0b...
    int_a = int(bin_a, 2)  # 0b... OR ... => int
