def haya():
    print ("[ HAYA ]")
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
    dic = {'hel':'HEL', 'e':'3', 'o':'0'}

    def find_and_replace(string, replacements):
        sorted_dict = sorted(replacements.keys(),key = len, reverse = True)
        for item in sorted_dict:
            if item in string:
                string = string.replace(item, replacements[item])
                return string

    print(find_and_replace(data, dic))
def a2e():
    data = input("Type or paste your Armenian script to be translated to English script.\n")

haya()
