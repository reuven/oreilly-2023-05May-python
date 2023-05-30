# I now have the count_vowels.py module
# it contains one thing: A function called count_vowels

# I'll need to import count_vowels
# I'll need to call count_vowels.count_vowels()

# if you try to call count_vowels(), you'll get an error -- module is "not callable"

def count_vowels(s):
    total = 0
    
    for one_character in s:
        if one_character in 'aeiou':
            total += 1
            
    return total