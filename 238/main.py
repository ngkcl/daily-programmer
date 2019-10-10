from collections import defaultdict
import random
import sys

words_by_letter_count = defaultdict(list)

def break_word_count():
    with open('enable1.txt') as f:
        for w in f.readlines():
            w = w.strip()
            words_by_letter_count[len(w)].append(w)

def guess(s, to_guess):
    c = 0
    for x,y in zip(s, to_guess):
        if x == y:
            c+=1
    return c

if __name__ == "__main__":
    dif = -1
    while dif <= 0 or dif > 5:
        dif = int(input('Select difficulty (1-5): '))

    break_word_count()

    word_count = 3 + dif*2
    word_len = 2 + dif*2

    random.shuffle(words_by_letter_count[word_len])
    
    words = words_by_letter_count[word_len][:word_count]
    to_guess = random.choice(words)

    print(*words, sep='\n')
    
    found = False
    guesses_left = 4
    while not found:
        if guesses_left <= 0:
            print('Game over')
            sys.exit()
        
        inp = input('Guess ({} left)? '.format(guesses_left))
        ans = guess(inp, to_guess)

        if ans == len(to_guess):
            found = True
        else:
            print('{}/{} correct'.format(ans, len(to_guess)))
        
        guesses_left -= 1
    
    print('You win!')