"""
for case if find caesar message bruteforce
"""

message = "GIEWIVrGMTLIVrHIQS"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(letters)):
    translated = ""
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(letters)
            translated = translated + letters[num]
        else:
            translated = translated + symbol
print("key #%s : %s" % (key, translated))
