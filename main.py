#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 2019-01-20
"""
import random
import argparse


lower_strings = 'abcdefghijklmnopqrstuvwxyz'
upper_strings = lower_strings.upper()
numbers = '0123456789'
symbols = '~!@#$%^&*()_+=-;",.<>/?\|{}[]'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--ln", type=int, default=0,
                        help="number of lower case letters")
    parser.add_argument("-u", "--un", type=int, default=0,
                        help="number of upper case letters")
    parser.add_argument("-n", "--nn", type=int, default=0,
                        help="number of upper case numbers")
    parser.add_argument("-s", "--sn", type=int, default=0,
                        help="number of symbols")
    args = parser.parse_args()

    rs = 'l'*args.ln + 'u'*args.un + 'n'*args.nn + 's'*args.sn
    la = [i for i in rs]
    random.shuffle(la)

    password = ''
    for i in la:
        if i == 'l':
            password += random.choice(lower_strings)
        elif i == 'u':
            password += random.choice(upper_strings)
        elif i == 'n':
            password += random.choice(numbers)
        else:
            password += random.choice(symbols)

    print(password)


if __name__ == '__main__':
    main()
