import constants

def checkChar(word:str):
	for charName in constants.specialChars:
		if (word=='*'+charName+'*'):
			return charName
	return False

def replaceSpecialsChars(source):
    for charName in constants.specialChars:
        element = constants.specialChars[charName]
        source = source.replace(element["regRule"], ' *'+charName+'* ')
    return source
