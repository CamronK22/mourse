#!/bin/python

import sys
import autopy

def dit():
    f = open("/tmp/data_mourse.txt", "a+")
    f.write(".")

def dah():
    f = open("/tmp/data_mourse.txt", "a+")
    f.write("-")

def back():
    f = open("/tmp/data_mourse.txt", "r+")
    code = f.read()[:-1]
    f = open("/tmp/data_mourse.txt", "w+")
    f.write(code)

def send():
    f = open("/tmp/data_mourse.txt", "r")
    try:
        autopy.key.type_string(morse[f.read()])
    except:
        print("Yikes. not a real character")
        exit(1)
    f = open("/tmp/data_mourse.txt", "w")
    f.write("")

morse = {'.-': 'a',   '-...': 'b',   '-.-.': 'c',
       '-..': 'd',      '.': 'e',   '..-.': 'f',
        '-.': 'g',   '....': 'h',     '..': 'i',
      '.---': 'j',    '-.-': 'k',   '.-..': 'l',
        '--': 'm',     '-.': 'n',    '---': 'o',
      '.--.': 'p',   '--.-': 'q',    '.-.': 'r',
       '...': 's',      '-': 't',    '..-': 'u',
      '...-': 'v',    '.--': 'w',   '-..-': 'x',
      '-.--': 'y',   '--..': 'z',  '-----': '0',
     '.----': '1',  '..---': '2',  '...--': '3',
     '....-': '4',  '.....': '5',  '-....': '6',
     '--...': '7',  '---..': '8',  '----.': '9'
}
argtree = {
    '.': dit,
    '-': dah,
    's': send,
    'b': back
}
argtree.get(sys.argv[1], lambda: exit("try . - s b"))()
