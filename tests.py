__author__ = 'Hasan Iqbal'

import unittest
from Scrabbler import Scrabbler

class ScrabblerTests(unittest.TestCase):
	def setUp(self):
		self.scrabbler = Scrabbler()

	def test_correct_anagrams(self):
		self.assertEquals(['absolve'], self.scrabbler.words_from_letters('olveabs'))
	
	def test_correct_prefix(self):
		self.assertTrue('abdicate' in self.scrabbler.words_with_prefix('ab'))

	def test_correct_suffix(self):
		self.assertTrue('onyx' in self.scrabbler.words_with_suffix('yx'))

if __name__ == '__main__':
    unittest.main()