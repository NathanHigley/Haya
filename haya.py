#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

print ("[ H A Y A ]\n\n")

def main():
    prompt = input("Type '1' to encrypt an English script into Armenian script. \nType '2' to decrypt an Armenian script into English script.\n")
    while (prompt != "1" and prompt != "2"):
        print ("Invalid.\n\n")
        main()
    data = input("Type or paste your script.\n")

    if (prompt == "1"):
        dic = {    'A':'Ա', 'a':'ա',
                   'B':'Բ', 'b':'բ',
                   'C':'Կ', 'c':'կ',#Defaults to K because I'm lazy.
                   'D':'Դ', 'd':'դ',
                   'E':'Ե', 'e':'ե',
                   'F':'Շ', 'f':'շ',
                   'G':'Ց', 'g':'g',
                   'H':'Հ', 'h':'h',
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
                   '1':'1', '2':'2',
                   '3':'3', '4':'4',
                   '5':'5', '6':'6',
                   '7':'7', '8':'8',
                   '9':'9', '0':'0',
                   ' ':' ', ',':',',
                   "'":"'", '"':'"'
                  }
    if (prompt == "2"):
        dic = {    'Ա':'A', 'ա':'a',
                   'Բ':'B', 'բ':'b',
                   'Դ':'D', 'դ':'d',
                   'Ե':'E', 'ե':'e',
                   'Շ':'F', 'շ':'f',
                   'Ց':'G', 'g':'g',
                   'Հ':'H', 'h':'h',
                   'Ի':'I', 'ի':'i',
                   'Ծ':'J', 'ծ':'j',
                   'Կ':'K', 'կ':'k',
                   'Լ':'L', 'լ':'l',#L doubler is omitted until I figure it out.
                   'Մ':'M', 'մ':'m',
                   'Ն':'N', 'ն':'n',
                   'Ո':'O', 'ո':'o',
                   'Թ':'P', 'թ':'p',
                   'Կղ':'Q', 'կղ':'q',
                   'Ր':'R', 'ր':'r',
                   'Ս':'S', 'ս':'s',
                   'Տ':'T', 'տ':'t',
                   'Ու':'U', 'ու':'u',
                   'Վ':'V', 'վ':'v',
                   'Ղ':'W', 'ղ':'w',
                   'ԿՍ':'X', 'կս':'x',
                   'Յ':'Y', 'յ':'y',
                   'Զ':'Z', 'զ':'z',
                   ':':'.', '՞':'?',
                   '1':'1', '2':'2',
                   '3':'3', '4':'4',
                   '5':'5', '6':'6',
                   '7':'7', '8':'8',
                   '9':'9', '0':'0',
                   ' ':' ', ',':',',
                   "'":"'", '"':'"'
                  }

    def replace(string, replacements):
        sorted_dict = sorted(replacements.keys(),key = len, reverse = True)
        for item in sorted_dict:
            if item in string:
                string = string.replace(item, replacements[item])
                return string

    print("-----------------------------------")
    for char in data:
        print(replace(char, dic), sep=' ', end='', flush=True)
    print ("\n")

main()
