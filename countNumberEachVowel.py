
vowel = 'aiueo'

setString = 'Hello, get back to the future'
setString = setString.casefold()

count = {}.fromkeys(vowel, 0)

for charCount in setString:
    if charCount in count:
        count[charCount] += 1
        
print(count)
