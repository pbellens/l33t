from interqu import valid_anagram as t


def test_01():
    assert(t.anagrams(s = 'anagram', t = 'nagaram') == True)

def test_02():
    assert(t.anagrams(s = 'rat', t = 'car') == False)
