def splitLen(seq, lenght):
    return [seq[i : i + lenght] for i in range(0, len(seq), lenght)]


def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)}


chiperText = ""

for index in sorted(order.keys()):
    for part in splitLen(plaintext, len(key)):
        try:
            chiperText += part[order[index]]
        except IndexError:
            continue

    return chiperText

print("message : zulkepretest make templest ostest")
print(encode("3124", "zulkepretes make templest ostest"))
