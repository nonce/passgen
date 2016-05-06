#!/usr/bin/env python
"""passgen.py: A Nemonic Password Generator."""

#######################################################################
# Special Thanks to Change, Smitty, and J05#! I can see so much more. #
#######################################################################

__author__    = "Nonce"
__copyright__ = "Copyright 2016"
__license__   = "GPL"
__version__   = "0.1.0"


import argparse
import random

wordlist = []

PUNC_LIST = [
    ',',
    '.',
    '=',
    '-',
    '/',
    '\\',
    '[',
    ']',
    '`',
    ';',
    "'",
    ' ',
    '!',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '?',
    '|',
    '{',
    '}',
    '~',
    ':'
]

NUM_LIST = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

L337_D1C7 = {
    "A": ['@', '4'],
    "B": ['8'],
    "C": ['[', '('],
    "E": ['3'],
    "G": ['6', '9'],
    "H": ['#'],
    "I": ['!', ],
    "L": ['1'],
    "O": ['0'],
    "S": ['$', '5'],
    "T": ['+', '7'],
    "Z": ['2']
}

L337_3X7_D1C7 = {
    "A": ['/-\\', '/_\\'],
    "B": ['|3'],
    "C": ['<', '{'],
    "D": ['!>', '|)', '|}', '|]'],
    "F": ['|=', 'ph'],
    "G": ['[,', '-,', '[+'],
    "H": ['|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],
    "I": ['|'],
    "K": ['|<', '1<'],
    "L": ['|_', '|'],
    "M": ['|\/|'],
    "N": ['|\|', '/\/'],
    "O": ['()', '[]', '{}'],
    "P": ['|o', '|O', '|>'],
    "Q": ['O', '9'],
    "R": ['|2', '12'],
    "U": ['|_|'],
    "V": ['\/'],
    "W": ['\/\/', '(/\)', '\^/', '|/\|'],
    "X": ['><'],
}


def get_rand_word(wordlist):
    return random.choice(wordlist)


def gen_pass(words, shift, wordlist, punc_list, prepend, interleave, postpend):
    pw = []
    word = ""

    punc = ""
    for p in punc_list:
        punc += p
    print "Allowed punctuation: " + punc + "\n"
    while words:
        c = get_rand_word(wordlist).split('\n')[0]
        if not shift:
            c = c.lower()
        pw.append(c)
        words -= 1

    if prepend:
        word += random.choice(punc_list)

    for w in pw:
        word += w
        if interleave:
            word += random.choice(punc_list)

    if not postpend:
        word = word[0:-1]

    return word


def main():
    parser = argparse.ArgumentParser("Generate N.M nemonic password")
    l33t3x = parser.add_mutually_exclusive_group()
    parser.add_argument("-0", "--prepend-punc",
                        help="begin password with punctuation. Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-1", "--postpend-punc",
                        help="end password with punctuation. Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-d", "--dictionary-path",
                        type=str,
                        help="path to \\n-delimited word list. Default: /usr/share/dict/words",
                        action="store",
                        default="/usr/share/dict/words")
    l33t3x.add_argument("-E", "--leet-extended",
                        help="allow extended l33t character substitution (http://www.securepasswords.net/site/ASCII-"
                             "1337-Alphabet/page/23.html). Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-H", "--shift",
                        help="allow characters requiring shift key. Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-I", "--interleave",
                        help="interleave words with punctuation. Default: True",
                        action="store_false",
                        default=True)
    l33t3x.add_argument("-L", "--leet",
                        help="allow basic l33t character substitution (http://www.securepasswords.net/site/ASCII-"
                             "1337-Alphabet/page/23.html). Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-N", "--numbers",
                        help="use Numbers as punctuation",
                        action="store_true",
                        default=False)
    parser.add_argument("-p", "--punc-list",
                        help="list of allowed punctuation.",
                        action="store",
                        default=PUNC_LIST,
                        nargs="*")
    parser.add_argument("-S", "--allow-space",
                        help="allow space to be a punctuation char. Default: False",
                        action="store_true",
                        default=False)
    parser.add_argument("-w", "--words",
                        type=int,
                        help="number of words. Default: 3",
                        action="store",
                        default=3)
    args = parser.parse_args()

    with open(args.dictionary_path, 'r') as wlfp:
        for w in wlfp:
            wordlist.append(w)

    if not args.shift:
        punc_list = args.punc_list[0:args.punc_list.index(" ") + 1]

    if not args.allow_space:
        punc_list.remove(" ")

    else:
        punc_list = PUNC_LIST

    if args.numbers:
        punc_list += NUM_LIST

    word = gen_pass(args.words, args.shift, wordlist, [p for p in args.punc_list if p in punc_list], args.prepend_punc,
                    args.interleave, args.postpend_punc)

    print "Suggestion: " + word

    l3w = ""

    if args.leet:
        for c in word:
            if c.upper() in L337_D1C7:
                l3w += random.choice(L337_D1C7[c.upper()])
            else:
                l3w += c.lower()

    if args.leet_extended:
        for c in word:
            if c.upper() in L337_3X7_D1C7:
                l3w += random.choice(L337_3X7_D1C7[c.upper()])
            else:
                l3w += c

    if l3w:
        print "L33T:       " + l3w


if __name__ == "__main__":
    main()
