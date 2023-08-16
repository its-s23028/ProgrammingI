num_list = list(range(1, 8))


def double(x):
    """与えられたオブジェクトを二倍する"""
    return x * 2


for e in map(double, num_list):
    print(e, end=" ")
