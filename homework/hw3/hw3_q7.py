# defining a function that takes an input of a string and
# outputs the number of values in that string

def vowelcount(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] # list of vowels to check
    count = 0 # initiating a count of vowels in word
    for i in word:
        for j in vowels: # nested for loop to compare each term to each vowel
            if i == j:
                count += 1
    return count