#NUMBER 1
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

input_string = "Hello World"
print(f"Length of the string: {string_length(input_string)}")

#NUMBER 2
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

input_string = "programming"
print(f"Character frequency: {char_frequency(input_string)}")

#NUMBER 3
def replace_first_char(s):
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '@')
    return modified_string

input_string = "apple application"
print(f"Modified string: {replace_first_char(input_string)}")

#NUMBER 4
def concat_and_swap(s1, s2):
    modified_string = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    return modified_string

string1 = "abc"
string2 = "xyz"
print(f"Modified string: {concat_and_swap(string1, string2)}")

#NUMBER 5
def remove_char_at_index(s, index):
    modified_string = s[:index] + s[index + 1:]
    return modified_string

input_string = "Hello World"
index_to_remove = 3
print(f"Modified string: {remove_char_at_index(input_string, index_to_remove)}")

#number 6
def swap_first_last(s):
    if len(s) < 2:
        return s  # No change for strings with length less than 2
    modified_string = s[-1] + s[1:-1] + s[0]
    return modified_string

input_string = "Python"
print(f"Modified string: {swap_first_last(input_string)}")

#number 7
def remove_odd_indices(s):
    modified_string = s[::2]
    return modified_string

input_string = "Computer Science"
print(f"Modified string: {remove_odd_indices(input_string)}")

#number 8
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

input_sentence = "Python is easy and Python is powerful"
print(f"Word frequency: {word_frequency(input_sentence)}")

#number 9
def convert_case(s):
    uppercase = s.upper()
    lowercase = s.lower()
    return uppercase, lowercase

input_string = "Hello World"
upper, lower = convert_case(input_string)
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

#number 10
def reverse_string(s):
    reversed_string = s[::-1]
    return reversed_string

input_string = "Python"
print(f"Reversed string: {reverse_string(input_string)}")

#number 12
def reverse_words(s):
    words = s.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

input_string = "Hello World"
print(f"Reversed words: {reverse_words(input_string)}")

#number 16
def uncommon_characters(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    uncommon_chars = set1.symmetric_difference(set2)
    return "".join(uncommon_chars)

string1 = "abcd"
string2 = "cdefg"
print(f"Uncommon characters: {uncommon_characters(string1, string2)}")

#number 18
def find_substring_index(s, substring):
    index = s.find(substring)
    return index

input_string = "Python is powerful"
substring_to_find = "is"
print(f"Index: {find_substring_index(input_string, substring_to_find)}")

