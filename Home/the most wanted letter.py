"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.
Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
"""

from collections import Counter
import re

def checkio(text):
    new_list = []
    final_list = []
    the_text_list = list(text)
    for item in the_text_list:
        if re.match("[a-zA-Z]", item) is not None:
            new_list.append(item)
    
    new_string = "".join(new_list) #new string has only letters
    b = new_string.lower() #only lowercase letters
    b = list(b)
    counter = Counter(b)
    b = counter.most_common(1)
    b = b[0]
    x, highest_value = b
    for i in counter:
        if counter[i] == highest_value:
            final_list.append(i)
    final_list.sort()
    return final_list[0]
    #return letter
    
    
    
    
    