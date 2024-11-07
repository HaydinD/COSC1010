#
# Haydin Davis
# 11/7
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
def main():
    user_str= input('Enter a string of characters: ')
    print('The string has',num_vowels(user_str),'vowels and',
          num_constonants(user_str),'constonants.')


def num_vowels(s):
    vowels=['a','e','i','o','u']
    v_count=0

    for ch in s:
        if ch.lower() in vowels:
            v_count +=1

    return v_count

def num_constonants(s):
    vowels=['a','e','i','o','u']
    c_count=0

    for ch in s:
        if ch.isalpha and ch.lower() not in vowels:
            c_count +=1

    return c_count
main()
