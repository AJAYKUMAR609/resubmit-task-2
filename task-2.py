# program to find number of vowels are there in a given string
def count_vowels(string):
    # Initialize counters for each vowel
    count_a = count_e = count_i = count_o = count_u = 0

    # Convert the string to lowercase to handle both upper and lower case vowels
    string = string.lower()

    # Iterate through each character in the string
    for char in string:
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

    # Calculate the total number of vowels
    total_vowels = count_a + count_e + count_i + count_o + count_u

    # Print the counts of each individual vowel and total number of vowels
    print("Count of 'A':", count_a)
    print("Count of 'E':", count_e)
    print("Count of 'I':", count_i)
    print("Count of 'O':", count_o)
    print("Count of 'U':", count_u)
    print("Total number of vowels:", total_vowels)


# Test the function with the given string
input_string = "Guvi geeks network private limited"
count_vowels(input_string)


# Define the number of rows for the pyramid
n= 20
# Outer loop for rows
for i in range(1, n + 1):
    # Print spaces for left alignment
    print(" " * (n - i), end="")

    # Inner loop for printing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line
    print()


# write a python program to print given string by removing vowels
def remove_vowels(input_string):
    # string containing all vowels of uppercase and lowercase
    vowels = "aeiouAEIOU"

    # Use list comprehension to create a new string with vowels removed
    new_string = ''.join(char for char in input_string if char not in vowels)

    return new_string

# Test the function
input_string = "Hello, World! This is a test string."
result = remove_vowels(input_string)
print("Original string:", input_string)
print("String with vowels removed:", result)

# check whether the given string is palindrome
s="madam"
s1=(s[::-1])
if s1==s:
    print("sting is palindrome")
else:
    print("string is not palindrome")


# check whether given strings are anagrams are not
s1= "lazy"
s2="zaly"
if sorted(s1)==sorted(s2):
    print("Both strings are anagrams")
else:
    print("both are not anagrams")


# to print longest common sub string
def str(X, Y):
    m, n = len(X), len(Y)
    str = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                str[i][j] = str[i - 1][j - 1] + 1
                result = max(result, str[i][j])
            else:
                str[i][j] = 0

    return result

# Example usage
X = "Hello this is ajaykumar"
Y = " hi ajaykumar"
print(f"Length of Longest Common Substring is {str(X, Y)}")

# to print most common character from a string
from collections import Counter
def most_frequent_char(s):
    counter = Counter(s)
    most_common = counter.most_common(1)[0]
    return most_common[0]

input_string = "keerthi ajay kumar"
result = most_frequent_char(input_string)
print(f"The most frequent character is: {result}")

# To print unique character from a string
def count_unique_chars(s):
    char_count = Counter(s)
    return len(char_count)

input_string = "ajay kumar"
result = count_unique_chars(input_string)
print(f"Number of unique characters: {result}")

# count number of words in a given string
def count_words(string):
    string1 = string.strip()
    count = 1  # Initialize count to 1 (no space at the end)
    for char in string1:
        if char == " ":
            count += 1
    return count

input_string = "Hi my name is ajay kumar i am from hyderbad"
print(f"'{input_string}' has {count_words(input_string)} words.")