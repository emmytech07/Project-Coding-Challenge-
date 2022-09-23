# Method 1
# def replace_word():
#     str = "This is a coding challenge"
#     word_replace = input('Enter word to replace ')
#     word_replacement = input('Enter the word replacement ')

#     print(str.replace(word_replace, word_replacement))

# replace_word()

# METHOD 2



def replace_word(string):
    word1 = str(input("Input your word to be replace in string: "))
    word2 = str(input('Replaced with string: '))
    
    print(string.replace(word1, word2))

replace_word("Possibilities is the order of the day")