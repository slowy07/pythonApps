#generators method 1
def set_gen(x):
    for x in range(x):
        yield x ** 3
"""
values = set_gen(100)
print(sys.getsizeof(values))
print(next(values))
print(next(values))
print(next(values))
for x in values:
    print(x)
"""

def unlimited_seq():
    result = 1
    while True:
        yield result
        result += 5

values = unlimited_seq()
print(next(values))
"""
for x in values:
    print(x)
"""