"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.

UPPER

input: array of words
str of chars in some order 
    -always 26 
    - no duplicates
output: boolean

Loops over each word
compare current word to next word
    -letter by letter
    -loop
    -find index in "order" (letters in alpha order)
    -find(), index, or loop over order
    -index_1, index_2
    -if index_1 <= index_2:
        continue
    -else return false
if sorted:
    continue
else:
    return false
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    alpha_dict = {}
    for i in range(len(alpha_order)):
        alpha_dict[alpha_order[i]] = i
    print(alpha_dict)


    # Loop over the array of words
    for i in range(len(words) -1):
        #look at two words at a time
        #word1, word2
        word1 = words[i]
        word2 = words[i +1]
        #compare word1 to word2
        #Go letter by letter of both words
        for j in range(min(len(word1), len(word2))):
            #letter1, letter2
            letter1 = word1[j]
            letter2 = word2[j]
            #find if letter1< letter2 using the apha_order
            if letter1 != letter2:
                if alpha_dict[letter1] > alpha_dict[letter2]:
                    return False
                    #break here
                break
            #If we got to the end of the loop and we didn't break, check the length of the words
        else:
            if len(word1) > len(word2):
                return False
                    #get index of letter1, get index of letter2
    return True


words = ["lambda", "school"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(are_words_sorted(words, order))



