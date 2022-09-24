# Have a key /value pair that represents a word and its definition
# Collect input form a uaer, input is a word
# Check if the word id in dictionary
# Print out the meaning 

def main():
    word_dictionary = {
        'go': 'meaning you should go',
        'come': 'meaning you should come ',
        'eat': 'take something in your stomach'
    }
    while(True):
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ' :', word_dictionary[word])

main()
