import os
import sys
import re

typeNumber  = "number"
typeWord    = "word"

specialChars = {
    "newLine":        {"regRule": "\n", "value":"\n"},
    "equal":          {"regRule": "=", "value":"="},
    "point":           {"regRule": ".", "value":"."},
    "virgule":           {"regRule": ",", "value":","},
    "quotationMark":  {"regRule": "\"", "value":"\"" },
    "openParenthese":  {"regRule": "(", "value":"("},
    "closeParenthese":  {"regRule": ")", "value":")"}
}

if len(sys.argv) < 2:
	print('you must supply an input file')
	quit()

def readFile():
	with open(sys.argv[1]) as file:
		source = file.read()
	print(source)
	return source

def checkChar(word:str):
	for charName in specialChars:
		if (word=='*'+charName+'*'):
			return charName
	return False

def replaceSpecialsChars(source):
    for charName in specialChars:
        element = specialChars[charName]
        source = source.replace(element["regRule"], ' *'+charName+'* ')
    return source

def tokenizer():
	source = readFile()
	new_source = replaceSpecialsChars(source)
	token_list = []
	new_source2 = re.split("[\t\f\v ]+", new_source)
	print(new_source2)
	for word in new_source2:
		if not word.isdigit():
		#if len(word)<=0 or word==None:
			typeChars = checkChar(word)
			if (typeChars):
				token_list.append({"type": typeChars})
			else:
				token_list.append({"type": typeWord, "value": word})
		else:
			token_list.append({"type": typeNumber, "value": word})
	
	if len(token_list)<1:
		print("PAS DE TOKEN !")
	for token in token_list:
		print(token)
	return token_list


tokenizer()