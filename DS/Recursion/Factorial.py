def factorial(n):

    #Base case
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)


print(factorial(5))



def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))


def sum_func(n):
    if n ==0:
        return 0
    else:
        return n %10+ sum_func(n//10)

print(sum_func(4321))


def sum_func1(n):

    if len(str(n)) ==1:
        return 1
    else:
        return n%10 + sum_func1(n//10)

print(sum_func1(4321))

# Create a function called word_split() which takes in a string
# phrase and a set list_of_words. The function will then determine
# if it is possible to split the string in a way in which words can be made
# from the list of words. You can assume the phrase will only contain words
# found in the dictionary if it is completely splittable.


def word_split(phrase,list_of_words, output = None):
    '''
    Note: This is a very "python-y" solution.
    '''
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in list_of_words:


        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):

            # Add the word to the output
            output.append(word)

            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)

    # Finally return output if no phrase.startswith(word) returns True
    return output


print(word_split('themanran',['clown','ran','man']))
print(word_split('themanran',['ran','the','man']))


print(word_split("themanran",["the","man","ran"]))

