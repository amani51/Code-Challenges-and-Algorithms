# Write here the code challenge solution
import re
def isValid(s):
    '''
    A function that takes a string s containing the characters 
    '(', ')', '{', '}', '[' and ']'
    And An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
    if its valid return True or False if it is not.
    '''
    open_brackets = []
    valid = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for c in s:
        if c.isalpha():
            s=s.replace(c,'')
    for i in s:
        if s[0] in valid:
            return False
        elif i not in valid:
            open_brackets.append(i)
        elif len(open_brackets) != 0:
            if open_brackets[-1] != valid[i]:
                return False
            elif open_brackets[-1] == valid[i]:
                open_brackets.pop()
        elif i in valid:
            return False
    return len(open_brackets) == 0 


if __name__ == '__main__':
    print('\n# #################### isValid function #################### #\n')
    print("==> isValid ('()') =>",isValid('()'),'\n')
    print("==> isValid (')(') =>",isValid(')('),'\n')
    print("==> isValid ('[({}]') =>",isValid('[({}]'),'\n')
    print("==> isValid '[[[{}]]]') =>",isValid('[[[{}]]]'),'\n') 
    print("==> isValid('[(hello)()]') =>",isValid('[(hello)()]'),'\n')
    print("==> isValid('[{(()}]') =>",isValid('[{(()}]'),'\n')
    print('# ######################################################### #\n')
