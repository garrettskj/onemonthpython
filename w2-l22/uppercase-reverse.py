#!/usr/bin/python3

def up_and_rev(text):
    # print original
    print (text)
    # UPPERCASE and then process backwards
    print ((text.upper())[::-1])

# banana
word = 'banana'

up_and_rev(word)

# FISH
word = 'FISH'

up_and_rev(word)
