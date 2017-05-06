__author__ = 'Hasan Iqbal'

import sys
from optparse import OptionParser
import itertools
from collections import Counter

class Scrabbler(object):
	'''
	Scrabbler class can return the matched words read from a dictionary. It also can return words 
	starting or ending with a specific sequence of letters. 
	'''

	def main(self):
		'''
		depending on the command line options, this method decides which method to call
		the options could have a option string or not. 
		'''

		if len(sys.argv) == 2: # no extra option was supplied
			print self.words_from_letters(sys.argv[1])
		else:
			parser = OptionParser()
			parser.add_option("--prefix", help="return words with this prefix")
			parser.add_option("--suffix", help="return words with this suffix")
			options, args = parser.parse_args()
			option_dict = vars(options)
			if option_dict['prefix']:
				print self.words_with_prefix(option_dict['prefix'])
			if option_dict['suffix']:
				print self.words_with_suffix(option_dict['suffix'])
	
	def words_from_letters(self, letters):
		'''
		find all words that could be formed using this set of letters.
		:type letters: set of letters
		:rtype: set of possible words		
		'''
		matched_words = []
		with open('words.txt') as file: # doesn't load the whole file. only one at a time
			for line in file:
				if len(line.strip()) == len(letters) and Counter(line.strip()) == Counter(letters): # length mathing convenient optimization. O(N)
					matched_words.append(line.strip())
		return matched_words


	def words_with_suffix(self, suffix):
		'''
		:type suffix string: sequence of letters to be searched in the dictionary. words should have suffix at the end
		'''
		matched_words = []		
		with open('words.txt') as file: # doesn't load the whole file. only one at a time
			for line in file:
				if line.strip().endswith(suffix):
					matched_words.append(line.strip())
		return matched_words

	def words_with_prefix(self, prefix):
		'''
		:type prefix string: sequence of letters to be searched in the dictionary. words should have prefix at the beginning
		'''		
		matched_words = []		
		with open('words.txt') as file: # doesn't load the whole file. only one at a time
			for line in file:
				if line.strip().startswith(prefix):
					matched_words.append(line.strip())
		return matched_words

if __name__ == "__main__":
	Scrabbler().main()