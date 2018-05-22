def haya():
    print ("[ HAYA | PLACE HOLDER]\n")
    prompt = input("Type '1' to translate English script to Armenian script. Type '2' to translate Armenian script to English script.\n")
    if (prompt == "1"):
        e2a()
    if (prompt == "2"):
        a2e()
    while (prompt != "1" and prompt != "2"):
        print ("Invalid.")
        prompt = input("Type '1' to translate English script to Armenian script. Type '2' to translate Armenian script to English script.\n")

def e2a():
    data = input("Type or paste your Armenian script to be translated to English script.\n")
    dic = {'A':'Ա', 'a':'ա', 
           'B':'', 'b':'',
           'C':'', 'c':'',
          }

    def fr(string, replacements):
        sorted_dict = sorted(replacements.keys(),key = len, reverse = True)
        for item in sorted_dict:
            if item in string:
                string = string.replace(item, replacements[item])
                return string

    print(fr(data, dic))
def a2e():
    data = input("Type or paste your Armenian script to be translated to English script.\n")
    dic = {'Ա':'A', 'ա':'a', 
           '':'B', '':'b',
           '':'C', '':'c',
          }

    def fr(string, replacements):
        sorted_dict = sorted(replacements.keys(),key = len, reverse = True)
        for item in sorted_dict:
            if item in string:
                string = string.replace(item, replacements[item])
                return string

    print(fr(data, dic))
haya()
