from collections import Counter, defaultdict
import itertools
import os

morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ')

def smorse(s):
    res = ''
    for l in s:
        index = int(ord(l) % 97) 
        # ord(a) % 97 = 
        res += morse[index]
    return res

if __name__ == '__main__':
    y = 0
    morse_count = Counter()
    # morse_to_word = defaultdict(list)
    with open(os.getcwd() + '/enable1.txt', 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if y < 10:
                    print('\'' + l + '\'')
                    y+=1
            
            m = smorse(l)

            # Find count of dashes and dots
            dash_counter = 0
            dash_in_row = 0
            dot_counter = 0
            for letter in m:
                if letter == '-':
                    dash_counter += 1
                    dash_in_row +=1 
                    if dash_in_row == 15:
                        print("word with 15 dashes is " + l)
                else:
                    dot_counter += 1
                    dash_in_row = 0
            
            # Find perfectly balanced words
            if dash_counter == dot_counter and len(l) == 21:
                print('{} is a 21 letter perfectly balanced word'.format(m))

            morse_count[m] += 1
    
    tested = []
    found = []
    comb = itertools.product(['-','.'], repeat = 13)

    for c in list(comb):
        c = ''.join(c)
        flag = False
        for w in morse_count.keys():
            if c in w:
                flag = True
                break
        if not flag:
            found.append(c)
            print(c)
    
    # Show the morse word that appears most often
    print(morse_count.most_common(1))