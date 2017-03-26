'''
Create an English to Portuguese translation program.

The program takes a word from the user as input and translates
 it using the following dictionary as a vocabulary source.
 In addition, try to return the message "We couldn't find that word!"
 when the user enters a word that is not in the dictionary.


Expected output:

Enter word: hello
We couldn't find that word!
'''

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def voc(word):
    try:
        return d[word]
    except KeyError :
        return "We couldn't find that word"

word = input("Enter a word ")
print(voc(word))