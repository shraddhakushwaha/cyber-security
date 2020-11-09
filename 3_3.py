def reversed_words(str):
    words=str.split(' ')
    reverse_sentence=' '.join(reversed(words))
    return reverse_sentence
a=input("enter the string:")
print(reversed_words(a))
