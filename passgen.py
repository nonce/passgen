#!/usr/bin/env python
"""passgen.py: A Nemonic Password Generator."""

#######################################################################
# Special Thanks to Change, Smitty, and J05#! I can see so much more. #
#######################################################################

__author__    = "Nonce"
__copyright__ = "Copyright 2016"
__license__   = "GPL"
__version__   = "0.1.0"


wordlist = []

DEFAULT_WORD_DICT = '/usr/share/dict/words'

PUNCT_LIST = [
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


def gen_pass(words, no_shift, wordlist, punct_list, prepend, interleave, postpend):
    pw = []
    word = ""

    punc = ""
    for p in punct_list:
        punc += p
    print "PUNCTUATION ALLOWED : " + punc
    print "SPACES ALLOWED      : {}".format(bool(' ' in punc))
    while words:
        c = get_rand_word(wordlist).split('\n')[0]
        if no_shift:
            c = c.lower()
        pw.append(c)
        words -= 1

    if prepend:
        word += random.choice(punct_list)

    for w in pw:
        word += w
        if interleave:
            word += random.choice(punct_list)

    if not postpend:
        word = word[0:-1]

    return word


def main():
    parser = argparse.ArgumentParser("Generate N.M nemonic password")
    pnctrl = parser.add_argument_group('punct_rules')
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
                        help="path to \\n-delimited word list. Default: {}".format(DEFAULT_WORD_DICT),
                        action="store",
                        default="/usr/share/dict/words")
    l33t3x.add_argument("-e", "--leet-extended",
                        help="allow extended l33t character substitution (http://www.securepasswords.net/site/ASCII-"
                             "1337-Alphabet/page/23.html). Default: False",
                        action="store_true",
                        default=False)
    pnctrl.add_argument("-H", "--no-shift",
                        help="disallow characters requiring shift key. Default: False",
                        action="store_true",
                        default=False)
    pnctrl.add_argument("-I", "--interleave",
                        help="interleave words with punctuation. Default: True",
                        action="store_false",
                        default=True)
    l33t3x.add_argument("-l", "--leet",
                        help="allow basic l33t character substitution Default: False",
                        action="store_true",
                        default=False)
    pnctrl.add_argument("-N", "--numbers",
                        help="use Numbers as punctuation",
                        action="store_true",
                        default=False)
    parser.add_argument("-p", "--punct-list",
                        help="list of allowed punctuation. NOTE: This argument overrides all 'punct_rules' arguments!",
                        action="store",
                        default=[],
                        nargs="*")
    pnctrl.add_argument("-S", "--no-spaces",
                        help="remove space to be a punctuation char. Default: False",
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

    if not args.punct_list:
        punct_list = PUNCT_LIST
        if args.no_shift:
            punct_list = punct_list[0:punct_list.index(' ') + 1]

        if args.no_spaces:
            punct_list.remove(' ')

        if args.numbers:
            punct_list += NUM_LIST
    else:
        punct_list = [p for p in args.punct_list if p in PUNCT_LIST]

    word = gen_pass(args.words, args.no_shift, wordlist, punct_list, args.prepend_punc,
                    args.interleave, args.postpend_punc)

    print "\nSUGGESTION : " + word

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
        print "L33T       : " + l3w


if __name__ == "__main__":
    main()
