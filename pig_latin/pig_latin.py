# Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix

# Rules:
# 1. For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added for example:
# "pig" = "igpay"
# "latin" = "atinlay"
# "banana" = "ananabay"
# "will" = "illway"
# "butler" = "utlerbay"
# "happy" = "appyhay"
# "duck" = "uckday"
# "me" = "emay"

# 2. For words that begin with vowel sounds, the vowel is left alone, and most commonly 'yay' is added to the end. But in different parts of the world, there are different 'dialects' of sorts. Some people may add 'way' or just 'ay' or other endings. Examples are:

# "eat" = "eatyay" or "eatay"
# "omelet" = "omeletyay" or "omeletay"
# "are" = "areyay" or "areay"
# "egg" = "eggyay" or "eggay"
# "explain" = "explainyay"
# "always" = "alwaysyay" or "alwaysay"
# "ends" = "endsyay" or "endsay"
# "honest" = "honestyay"
# "I"= "Iyay"

# 3. When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing.

# "smile" = "ilesmay"
# "string" = "ingstray"
# "stupid" = "upidstay"
# "glove" = "oveglay"
# "trash" = "ashtray"
# "floor"= "oorflay"
# "store"= "orestay"

# 4. An alternative convention for words beginning with vowel sounds, one removes the initial vowel(s) along with the first consonant or consonant cluster. This usually only works for words with more than one syllable and offers a variant of the words in keeping with the mysterious, unrecognizable sounds of the converted words. Examples are:

# "every" = "eryevay"
# "another" = "otheranay"
# "under" = "erunday"
# "island" = "andislay"
# "elegant" = "egantelay"

# for more, read >>> https://en.wikipedia.org/wiki/Pig_Latin

#! python3
# piglatin.py - a program to translate English words to pig latin

def pig_latin():
    text = input("Enter an English text to translate to Pig Latin: ")

    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y') # constant to store vowel sounds

    pig_latin_list = [] # list to store the words in Pig Latin language
    for word in text.split():
        prefix_non_letters = '' # a string to store non-letter characters at the beginning of the word
        while len(word) > 0 and not word[0].isalpha(): 
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0: # if the whole word is made of non-letters, add it to the pig_latin_list and continue to next word
            pig_latin_list.append(prefix_non_letters)
            continue

        suffix_non_letters = '' # a string to store non-letter characters at the end of the word
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]
        
        # Remember if word was uppercase or titlecase to convert back later
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower() # convert word to lowercase for translation

        prefix_consonants = '' # variable to store consonant sounds that appear at the beginning of the word
        while len(word) > 0 and word[0] not in VOWELS:
            prefix_consonants += word[0] # remove consonant sounds from beginning of word
            word = word[1:]

        # translate word to Pig Latin
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # add translated word to pig_latin_list
