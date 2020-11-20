string = 'arfy' #create string

#get looping
for letter in string:
    print(letter)
    #if letter contain a or y
    if letter == 'a' or letter == 'y':
        break
    print("stop looping")

i = 0
#create looping 
while True:
    print(letter[i])
    #if letter contain a or y
    if letter[i] == 'a' or letter[i] == 'y':
        break
    i += 1

print("stop looping")

