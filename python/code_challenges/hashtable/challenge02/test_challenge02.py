# Write your test here
from challenge02 import first_repeated_word
# #################### test first_repeated_word Function #################### #

def test_first_repeated_word():
    assert first_repeated_word('HELLO WORLD WORLD HELLO')=='WORLD'
    assert first_repeated_word('WORLD HELLO')=='No Repetition'
    assert first_repeated_word('WORLD HELLO HELLO WORLD')=='HELLO'
    assert first_repeated_word('No Repetition :p')=='No Repetition'

