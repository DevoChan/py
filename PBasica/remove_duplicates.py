
def remove_duplicates (word):
    new_word = ""
    for i in word:
        if i not in new_word:
            new_word += i
    return new_word

word = input("Type a word: ")
print (remove_duplicates(word))