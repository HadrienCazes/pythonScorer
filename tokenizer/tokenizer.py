import os
import sys
import re
from tokenizer import helper
from tokenizer import constants

if len(sys.argv) < 2:
	print('you must supply an input file')
	quit()

def readFile():
	with open(sys.argv[1]) as file:
		source = file.read()
	print(source)
	return source

def tokenizer():
	source = readFile()
	new_source = helper.replaceSpecialsChars(source)
	token_list = []
	new_source2 = re.split("[\t\f\v ]+", new_source)
	print(new_source2)
	for word in new_source2:
		if not word.isdigit():
		#if len(word)<=0 or word==None:
			typeChars = helper.checkChar(word)
			if (typeChars):
				token_list.append({"type": typeChars})
			else:
				token_list.append({"type": constants.typeWord, "value": word})
		else:
			token_list.append({"type": constants.typeNumber, "value": word})
	
	if len(token_list)<1:
		print("PAS DE TOKEN !")
	for token in token_list:
		print(token)
	return token_list