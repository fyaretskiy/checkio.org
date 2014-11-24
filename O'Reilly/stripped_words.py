"""
Our robots are always working to improve their linguistic skills. For this mission, they research the latin alphabet and its applications.
The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z
You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.
Input: A text as a string (unicode)
Output: A quantity of striped words as an integer.
Precondition:The text contains only ASCII symbols.
0 < len(text) < 105
"""

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import re

def checkio(text):
    binary_list = []
    count = 0
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    print("text1", text)
    text = text.upper()
    #quickly remove all words with numbers
    
    text = text.split(" ")
    temp_list = [] #ill gather unwanted number items here to remove later
    for word in text:
        if re.search("[0-9]", word) is not None:
            temp_list.append(word) #the iteration problem
    print("my temp list", temp_list) #ok templist works
    for item in temp_list:
        if item in text:
            text.remove(item)
    text = " ".join(text)
    
    #finished here with removing numbers
    text = re.sub("[AEIOUY]", "0", text)
    text = re.sub("[BCDFGHJKLMNPQRSTVWXZ]", "1", text)    
    binary_list = text.split(" ")
    
    for i in binary_list:
        if not "0" in i or not "1" in i:
            binary_list.remove(i)
    
    for word in binary_list: 
        i = 0 # cycle through each letter until letter = len - 2
        if len(word) == 1:
            binary_list.remove(word)
        while i <= (len(word)-2):
            if word[i] != word[i+1]:
                if i == (len(word)-2):
                    count += 1
                    break
                i += 1
            else:
                break
        
    print(count)
            
                
    
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
