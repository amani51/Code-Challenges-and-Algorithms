# Write here the code challenge solution
def first_repeated_word(words):
    '''
    A function that takes string as argument and returns the first repeated word 
    or returns "No Repetition" if there is no repeated word...
    '''
    rep = set()
    for word in words.split():
        if word in rep:
            return word
        else:
            rep.add(word)
    return 'No Repetition'


if __name__ == '__main__':
    print('\n# #################### first_repeated_word function #################### #\n')
    x="ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    print('> ',x)
    print('\n\tthe first repeated word => ',first_repeated_word(x))
    print('\n***********************************************************')
    y="I am learning programming at ASAC."
    print('> ',y)
    print('\n\tthe first repeated word => ',first_repeated_word(y))
    print('\n***********************************************************')
    z="Keep clam and Python is the best language B) Python OH-YAH"
    print('> ',z)
    print('\n\tthe first repeated word => ',first_repeated_word(z))
    print('\n***********************************************************')
