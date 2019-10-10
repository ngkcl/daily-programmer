morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
morse_dict = dict(zip(morse, alphabet))

running = True

def decode(word, result=""):
    global running
    if not running:
        return

    if word == '':
        yield result
        running = False
    
    for i in range(5,1,-1):
        if i > len(word):
            continue
            
        chunk = word[:i]
        if chunk in morse_dict:
            yield from decode(word[i:], result + morse_dict[chunk])

with open('smorse2-bonus1.in', 'r') as f:
    l = f.readline()
    for l in f.readlines():
        l = l.strip()

        running = True
        print(list(decode(l))[0])


