# project2.py
# Andrew Saad, 5/1/15



# function to determine if a sentence is a panagram or not

def isPangram(sentence):
    sentencel = sentence.lower()                                        # to eliminate case discrepancy
    answer = True                                                       # default answer is True
    for i in range(97,123):                                             # count through all lowercase letters
        if sentencel.count(chr(i)) == 0:                                # if any letter is missing
            answer = False                                              # change answer to False
    return answer




# function to determine if some text is a palindrome or not

def isPalindrome(text):
    textl = text.lower()                                                # to eliminate case discrepancy
    for i in range(len(textl)):                         
        if 97 > ord(textl[i]) or ord(textl[i]) > 122:   
            textl = textl.replace(textl[i],'.')                         # replace all non-alphabet characters with '.'
    raw_text = textl.replace('.','')                                    # remove all '.'
    answer = True                                                       # default answer is True
    for i in range(len(raw_text)//2):
        if raw_text[i] != raw_text[len(raw_text)-1-i]:                  # checks if first half == reverse of last half
            answer = False
    return answer




# functions to convert sentences to Pig Latin

vowels = 'AaEeIiOoUu'                                                   # strings containing useful characters
consonants = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz'
y = 'Yy'

def no_qu(word):                                                        # base function for translating words
    if word[0] in vowels:                                               # special case: word starts with vowel
        word = word + 'way'
        return word
    else:
        for i in range(len(word)):
            if word[i] in vowels + y:                                   # word starts with consonant, now count 'y' as a vowel
                word = word[i:] + word[:i] + 'ay'
                return word
        else:                                                           # word contains no vowels
            return word + 'ay'

def pigWord(word):                                                      # function to include special cases
    q = 'Qq'
    u = 'Uu'
    if word.islower():                                                  # if word is all lower case
        for i in range(len(word)):
            if word[0] in y:                                            # if word starts with 'y'
                word = word[1:] + word[0]                          
                if word[0] in vowels:                                   # and next letter is a vowel
                    return word + 'ay'
                else:                                                   # and next letter is not a vowel
                    return no_qu(word)
            if word[i] in u and word[i-1] in q:                         # if word contains 'qu'
                word = word[i+1:] + word[:i+1]                          
                if word[0] in vowels:                                   # and next letter is a vowel
                    return word + 'ay'
                else:                                                   # and next letter is not a vowel
                    return no_qu(word)
        else:
            return no_qu(word)
    elif word.isupper():                                                # if word is all upper case
        word = word.lower()
        for i in range(len(word)):
            if word[0] in y:
                word = word[1:] + word[0]
                if word[0] in vowels:
                    return word.upper() + 'AY'
                else:
                    return no_qu(word).upper()
            if word[i] in u and word[i-1] in q:
                word = word[i+1:] + word[:i+1]
                if word[0] in vowels:
                    return word.upper() + 'AY'
                else:
                    return no_qu(word).upper()
        else:
            return no_qu(word).upper()
    elif word[0].isupper():                                             # if word is properly capitalized (first letter capitalized, rest not)
        word = word.lower()
        for i in range(len(word)):
            if word[0] in y:
                word = word[1:] + word[0]
                if word[0] in vowels:
                    return word[0].upper() + word[1:] + 'ay'
                else:
                    return no_qu(word)[0].upper() + no_qu(word)[1:]
            if word[i] in u and word[i-1] in q:
                word = word[i+1:] + word[:i+1]
                if word[0] in vowels:
                    return word[0].upper() + word[1:] + 'ay'
                else:
                    return no_qu(word)[0].upper() + no_qu(word)[1:]
        else:
            return no_qu(word)[0].upper() + no_qu(word)[1:]

def pigLatin(text):                                                     # function to translate any string of letters and characters into Pig Latin  
    text = '!' + text + '!'                                             # ensures that word has more strings of symbols than letters
    symbols = ['a']*len(text)                                           # 'empty' list to fill with symbols, letter as placeholder
    letters = ['.']*len(text)                                           # 'empty' list to fill with letters, symbol as placeholder
    for i in range(len(text)):                                          # separates text into symbol list and letter list
        if text[i] in vowels + consonants + y:
            letters[i] = text[i]
        else:
            symbols[i] = text[i]
    symbol_string = ''
    letter_string = ''
    for item in symbols:                                                # creates string of symbols
        symbol_string = symbol_string + item
    for item in letters:                                                # creates string of letters
        letter_string = letter_string + item
    symbol_list = symbol_string.split('a')                              # creates list of groups of symbols
    symbol_groups = []
    for i in range(len(symbol_list)):                                   # removes all empty elements
        if symbol_list[i] != '':
            symbol_groups = symbol_groups + [symbol_list[i]]
    letter_list = letter_string.split('.')                              # creates list of groups of letters (words)
    letter_groups = []
    for i in range(len(letter_list)):                                   # removes all empty elements
        if letter_list[i] != '':
            letter_groups = letter_groups + [letter_list[i]]
    word_list = []
    for item in letter_groups:                                          # translates all words in list
        word_list = word_list + [pigWord(item)]
    word_list = word_list + ['']                                        # makes list of words and list of symbol groups same length (see first line)
    piglatin = ''
    for i in range(len(symbol_groups)):                                 # creates translated sentence
        piglatin = piglatin + symbol_groups[i] + word_list[i]
    return piglatin[1:len(piglatin)-1]                                  # removes the '!' added at the beginning

