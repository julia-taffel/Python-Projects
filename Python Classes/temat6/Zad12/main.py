def bin_to_dec(*args):
    result = 0
    for i, bit in enumerate(args):
        result += bit * (2 ** i)
    yield result