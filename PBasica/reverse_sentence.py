def print_reverse(sentence):
    for i in reversed (sentence):
        print(i, end = "")
sentence = input("write a sentence: ")
print_reverse(sentence)