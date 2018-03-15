str = "I am , a human, but ,'oh,ho', ar you"

print(str.find(","))
# print(str[str.find(",")::])

for word in str.split(","):
    if word[0] in '\'':
        print(word)