#
# Haudin Davis  
# 11/7
# Pig Latin Programming Project
# COSC 1010
#
i= 0
phrase = input('Enter a phrase: ').split(" ")
for word in phrase:
    word = list(word)
    word.append(word[0] + "AY")
    word.pop(0)
    phrase[i] = "".join(word)
    i+=1
print(" ".join(phrase))
