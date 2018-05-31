#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

print ("[ H A Y A ]\n\n")
prompt = input("Type '1' to encrypt an English script into Armenian script. \nType '2' to decrypt an Armenian script into English script.\n")
while (prompt != "1" and prompt != "2"):
    print ("Invalid.\n\n")
    prompt = input("Type '1' to encrypt an English script into Armenian script. \nType '2' to decrypt an Armenian script into English script.\n")
data = input("Type or paste your script.\n")

if (prompt == "1"):
    dic = {    'A':'Ա', 'a':'ա',
               'B':'Բ', 'b':'բ',
               'C':'Կ', 'c':'կ',#Defaults to K because I'm lazy.
               'D':'Դ', 'd':'դ',
               'E':'Ե', 'e':'ե',
               'F':'Շ', 'f':'շ',
               'G':'Ց', 'g':'ց',
               'H':'Հ', 'h':'հ',
               'I':'Ի', 'i':'ի',
               'J':'Ծ', 'j':'ծ',
               'K':'Կ', 'k':'կ',
               'L':'Լ', 'l':'լ',#L doubler is omitted until I figure it out.
               'M':'Մ', 'm':'մ',
               'N':'Ն', 'n':'ն',
               'O':'Ո', 'o':'ո',
               'P':'Թ', 'p':'թ',
               'Q':'Կղ', 'q':'կղ',
               'R':'Ր', 'r':'ր',
               'S':'Ս', 's':'ս',
               'T':'Տ', 't':'տ',
               'U':'Ու', 'u':'ու',
               'V':'Վ', 'v':'վ',
               'W':'Ղ', 'w':'ղ',
               'X':'ԿՍ', 'x':'կս',
               'Y':'Յ', 'y':'յ',
               'Z':'Զ', 'z':'զ',
               '.':':', '?':'՞',
               ' ':' '
              }
if (prompt == "2"):
    dic = {    'Ա':'A', 'ա':'a',
               'Բ':'B', 'բ':'b',
               'Դ':'D', 'd':'դ',
               'Ե':'E', 'e':'ե',
               'Շ':'F', 'f':'շ',
               'Ց':'G', 'g':'ց',
               'Հ':'H', 'h':'հ',
               'Ի':'I', 'i':'ի',
               'Ծ':'J', 'j':'ծ',
               'Կ':'K', 'k':'կ',
               'Լ':'L', 'l':'լ',#L doubler is omitted until I figure it out.
               'Մ':'M', 'մ':'m',
               'Ն':'N', 'ն':'n',
               'Ո':'O', 'ո':'o',
               'Թ':'P', 'թ':'p',
               'Կղ':'Q', 'կղ':'q',
               'Ր':'R', 'ր':'r',
               'S':'Ս', 's':'ս',
               'Տ':'T', 'տ':'t',
               'Ու':'U', 'ու':'u',
               'Վ':'V', 'վ':'v',
               'Ղ':'W', 'ղ':'w',
               'ԿՍ':'X', 'կս':'x',
               'Յ':'Y', 'յ':'y',
               'Զ':'Z', 'զ':'z',
               ':':'.', '՞':'?',
               ' ':' '
              }

def main():
    print("-----------------------------------")
    for char in data:
        print(fr(char, dic), sep=' ', end='', flush=True,)
    print ("\n")

def fr(string, replacements):
    sorted_dict = sorted(replacements.keys(),key = len, reverse = True)
    for item in sorted_dict:
        if item in string:
            string = string.replace(item, replacements[item])
            return string

main()
