# Python-Essentials-LAB-2.5.1.8-Anagrams

**Objectives**

•	improving the student's skills in operating with strings;

•	converting strings into lists, and vice versa.

**Scenario**

An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

•	asks the user for two separate texts;

•	checks whether, the entered texts are anagrams and prints the result.

Note:

•	assume that two empty strings are not anagrams;

•	treat upper- and lower-case letters as equal;

•	spaces are not taken into account during the check - treat them as non-existent

Test your code using the data we've provided.

**Test data**

*Sample input:*
```
Listen
Silent
```

*Sample output:*
```
Anagrams
```

*Sample input:*
```
modern
norman
```

*Sample output:*
```
Not anagrams
```

**Complete code includes**
```
input_line(ordinal):
    # checks user input and returns string; 
    # parameter 'ordinal' is to enumerte inputs;
    # returns string;

user_input():
    # This function sequentially prompts the user for two strings
    # and checks the equality of their lengths.
    # Returns tuple with two strings.

is_anagram(text1, text2):
    # Main algorithm that accepts string and returns True if string is a palindrome.
    # Returns True if inputs are palindromes

tests():
    # typical code that tries test cases
```

**implementations**

anagrams-v1.py - solves the problem in 7 strings of code

anagrams-v2.py - solves the problem in 4 strings of code
