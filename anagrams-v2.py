#This is the Python Essentials 2 LAB 2.5.1.8 Anagrams

def input_line(ordinal):
    # This function prompts the user and validates the input
    # Parameter 'ordinal' is to enumerte inputs
    # It returns a string in lower case without spaces
    # It checks user input for alphanumeric characters and spaces
    # Blank lines are not allowed
    while True:
        text = input("Enter " + ordinal + " line of text to check (Roman alphabet only): ")
        text = text.replace(" ", "")  # spaces are allowed
        if not text.isalpha():        # only alphabetic characters are allowed
            print("Invalid input. Only alphabetic characters and spaces are allowed.")
        elif len(text) == 0:          # blank lines are not allowed
            print("Invalid input. Blank lines are not allowed.")
        else:
            break
    return text

def user_input():
    # This function sequentially prompts the user for two strings
    # and checks the equality of their lengths.
    # Returns tuple with two strings.
    while True:
        text1 = input_line("first")               # first line to check 
        text2 = input_line("second")              # second line to check
        if len(text1) != len(text2):
            print("The lines must contain the same number of characters.")
        else:
            return text1, text2

def is_anagram(text1, text2):
    # Main algorithm that accepts string and returns True if string is a palindrome.
    # Palindrome is a word which look the same when read forward and backward.
    # For example, "kayak" is a palindrome, while "loyal" is not.
    # Returns True if inputs are palindromes
    text1 = text1.lower()                # treat upper- and lower-case letters as equal
    text2 = text2.lower()                # 
    text1 = text1.replace(" ", "")       # spaces are allowed
    text2 = text2.replace(" ", "")       # 
    if len(text1) != len(text2):         # only strings of same length allowed
        return False                     # if the lengths differ -> terminate function
    list1 = list(text1)                  # convert string into list
    list2 = list(text2)                  # 
    list1.sort()                         # sort the list
    list2.sort()                         #
    return list1 == list2                # no extra checks needed. Job is done


def tests():
    # typical code that tries test cases
    print("Self-test ...")
    test_texts1 = ("Listen",
                   "modern",
                   "Listen",
                   "Li st en")
    test_texts2 = ("Silent",
                   "norman",
                   "Silents",
                   "Si  le  nt")
    test_results = (True,
                    False,
                    False,
                    True)
    for i in range(len(test_texts1)):
        txt1 = test_texts1[i]
        txt2 = test_texts2[i]
        result = is_anagram(txt1, txt2)
        print(txt1 + ",", txt2, "->", result, end=" ")
        if result == test_results[i]:
                print("OK")
        else:
                print("Failed")


# Main
if __name__ == "__main__":
    text1, text2 = user_input()
    if is_anagram(text1, text2):
        print("Anagrams")
    else:
        print("Not anagrams")

##tests() # uncomment to perform self-test
