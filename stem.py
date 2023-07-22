import colorama
from colorama import Fore
def find_stemm(word):
    word=word.lower().lstrip().rstrip()
    word=remPref(word)
    word=remSuf(word)
    return word

def find_stemm_noun(word):
    nPref=['cha','che','vya','vye','ma','mi','mu','vi','zi','ki','wa','ya','m','n','u']
    nSuf=['ji','a','o','u','i','e']
    word=word.lower().lstrip().rstrip()
    for w in nPref:
        if word.startswith(w):
            word=word[len(w):]
            break
    for w in nSuf:
        if word.endswith(w) and len(word)>(len(w)):
            word=word[:len(word)-len(w)]
            break
    return word
def remPref(word):
    prefP=['a','ha','wa','ya','vi','ki','li','u','mu','ni','tu',
           'm','n','i','zi','ku','pa','na','si','hu'] #nafsi mtenda
    prefT=['na','li','ta','me','ka','ki','ku','ja','i','to','pa','si'] #wakati
    pref=['ngeli','ngali','nge','sha','ta','nyo','cho','ji','po','ye','mw','ny','ea','mi'] #
    prefMt=['wa','ya','vi','ki','li','mu','ni','tu','zi','ku','pa','m'] #nafsi mtendwa
    rem = []
    for w in prefP:
        if word.startswith(w):
            word=word[len(w):]
            rem.append(w)
            if w != 'ha':
                break
    for w in prefT:
        if word.startswith(w) and w not in rem and len(word)>(len(w)):
            word=word[len(w):]
            rem.append(w)
            break
    for w in pref:
        if word.startswith(w) and w not in rem and len(word)>(len(w)):
            word=word[len(w):]
            rem.append(w)
            break
    for w in prefMt:
        if word.startswith(w) and len(word)>(len(w)):
            word=word[len(w):]
            rem.append(w)
            break
    return word
def remSuf(word):
    suf1=['ishana','eleana','eshwa','liana','iliwa','ishwa','elewa','eleka','ezana',
          'isha','zana','eana','iana','liwa','jika','lika','shwa','iana','isha','esha',
          'sha','lia','jia','iwa','ana','ika','eni','ia','ka','ea','a','e','i','o']    #'ewa','mwa','ama','eza','eka','wa'
    suf2=['esh','ish','lio','ele','ez','ik','ew','iw','ek','iz','an','eo','io',
         'ji','vu','fu','el','sh','di','w']
    for w in suf1:
        if word.endswith(w) and len(word)>(len(w)):
            word=word[:len(word)-len(w)]
            break
    for w in suf2:
        if word.endswith(w) and len(word)>(len(w)):
            word=word[:len(word)-len(w)]
            break
    return word

print(Fore.RED + "1: verbs, 2: noun, * to select new choice, -1 to terminate :... ")
text=input("Enter your choice: ")
while text != "-1":
    if text == "1":
        text=input(Fore.BLUE + "Enter a verb:")
        while text != "*":
            print(Fore.BLUE + find_stemm(text))
            text=input(Fore.BLUE + "Enter a verb:")
    elif text == "2":
        text=input(Fore.GREEN + "Enter a noun:")
        while text != "*":
            print(Fore.GREEN + find_stemm_noun(text))
            text=input(Fore.GREEN + "Enter a noun:")
    print(Fore.RED + "1: verbs, 2: noun, * to select new choice, -1 to terminate :... ")
    text=input("Enter your choice: ")
