"""
We are using python3
"""


def shuffle(x):
    if x < 100:
        return x
    t = x
    l = 0
    while t > 0:
        t //= 10
        l += 1
    a = x // 10 ** (l - 1) * 10 ** (l - 1)
    b = (x % 10) * 10 ** (l - 2)
    return a + b + shuffle((x - a) // 10)


print(shuffle(123456))
print(shuffle(5444574147))
print(shuffle(3257423543222))

