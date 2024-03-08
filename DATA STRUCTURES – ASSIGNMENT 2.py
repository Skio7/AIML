# 1. Get a sentence from the user. Count the number of vowels and consonants in the sentence and store it in the form of dictionary.
def count_vowels_and_consonants(sentence):
    vowels = 0
    consonants = 0
    vowel_list = "aeiouAEIOU"
    for char in sentence:
        if char.isalpha():
            if char in vowel_list:
                vowels += 1
            else:
                consonants += 1
    return {'vowels': vowels, 'consonants': consonants}

user_sentence = input("Enter a sentence: ")
result = count_vowels_and_consonants(user_sentence)
print(result)

# 2. Get a sentence from the user. Extract only the unique words from the sentence in the form of list. Ignore the case while extracting the unique words.
def extract_unique_words(sentence):
    words = sentence.lower().split()
    unique_words = list(set(words))
    return unique_words

user_sentence = input("Enter a sentence: ")
unique_words_list = extract_unique_words(user_sentence)
print(unique_words_list)
# 3. Get a sentence from the user. Count the number of uppercase characters and lowercase 
# characters in the sentence, in the form of dictionary.
def count_uppercase_lowercase(sentence):
    uppercase_count = 0
    lowercase_count = 0
    for char in sentence:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return {'uc': uppercase_count, 'lc': lowercase_count}

user_sentence = input("Enter a sentence: ")
result = count_uppercase_lowercase(user_sentence)
print(result)

# 4. Get a sentence from the user. Extract only the uppercase characters from the sentence in 
# the form of tuple.

def extract_uppercase_characters(sentence):
    uppercase_chars = tuple(char for char in sentence if char.isupper())
    return uppercase_chars

user_sentence = input("Enter a sentence: ")
uppercase_tuple = extract_uppercase_characters(user_sentence)
print(uppercase_tuple)

# 5. Create a list that contains a collection of strings. Filter the list which contains only 
# Palindrome.
def is_palindrome(word):
    return word == word[::-1]

def filter_palindromes(word_list):
    return [word for word in word_list if is_palindrome(word)]

n = int(input("Enter the number of elements: "))
ls = []
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    ls.append(element)

palindrome_words = filter_palindromes(ls)
print(palindrome_words)
# 6. Create a Python Script to implement STACK. (Hint: LIFO – Last In First Out, i.e., The element 
# which is inserted last have to be removed first)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Stack after pop:", stack.items)
print("Peek:", stack.peek())
print("Size:", stack.size())
# 7. Create a Python Script to implement QUEUE. (Hint: FIFO – First In First Out, i.e., The element 
# which is inserted first have to be removed first)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.items)
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.items)
print("Size:", queue.size())
# 8. Get a string from the user. Count the number of occurrences of each character in the string 
# and store it in the form of dictionary.
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

user_string = input("Enter a string: ")
result = count_characters(user_string)
print(result)

# 9. Get a sentence from the user. Count the number of occurrences of each word in the 
# sentence and store it in the form of dictionary. Don’t ignore the case while counting.
def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

user_sentence = input("Enter a sentence: ")
result = count_word_occurrences(user_sentence)
print(result)
# 10. Get a string from the user. Extract the character which has most number of occurrences in 
# the string.
def most_common_character(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_char = max(char_count, key=char_count.get)
    return "character '{}' with '{}' occurrences".format(max_char, char_count[max_char])

user_string = input("Enter a string: ")
result = most_common_character(user_string)
print(result)