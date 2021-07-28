"""
Functions
Function returns a result:
*function terminates at return ans returns a value to invoking func.

>>> bool('something') -- returns True or False
>>> set()  -- empty set 
>>> {}     -- empty dictionary

** Parameters and Arguments
i. positional argument
ii. keyword arguments -- invoke a func passing keyword arguments


"""




def search_4_vowel(word : str) -> set:  # Annotation 
    """
    Returns any vowels found in a supplied word.
    """
    vowels = set('aeiou')
    # found = vowels.intersection(set(word))
    return vowels.intersection(set(word))
    
    # for vowel in found:
    #     # print(vowel)
    #     return bool(found)

print(search_4_vowel("Hello there !"))


def search4letters(phrase : str, letters : str = 'aeiou') -> set:
    """
    Search for any letters in a given phrase.

    """
    return (set(letters).intersection(set(phrase)))

# print(search4letters( " I am Mac Donald")) # positional argument
print(search4letters( phrase =" I am Mac Donald")) #keyword argument

