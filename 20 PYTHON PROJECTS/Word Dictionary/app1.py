# Working with pyDictionary
# pip install Py-Dictionary
# dict = Dictionary("Tragedy")
# meanings_list = dict.meanings()

# synonyms_list = dict.synonyms()

# antonyms_list = dict.antonyms()
# print(meanings_list)
# print(synonyms_list)

from pydictionary import Dictionary
while(True):
    word = input("Enter a word: ")
    container = Dictionary(word)
    if word == "":
        break
    print(container.synonyms())
    