from word_searching import word_search
import unittest

class word_test(unittest.TestCase):
    def test_word(self):
        doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
        self.assertEqual(word_search(doc_list,'casino'), [0])

unittest.TestCase()