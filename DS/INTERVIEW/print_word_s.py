'''
st = 'Print only the words that start with s in this sentence'

'''

st = "Print only the words that start with s in this sentence"

for word in st.split():
     if word[0] == 's':
         print(word)


'''
Go through the string below and if the length of a word is even print "even!"

'''

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 ==0:
        print (word ,"<-- has an even length")


'''
Use List Comprehension to create a list of the first letters of every word in the string below:
'''

st = 'Create a list of the first letters of every word in this string'

print([word[0] for word in st.split()])