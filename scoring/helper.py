from tokenizer import constants as constTokens

def numberLines(tokens):
    # Nb de lignes < 200
    cpt = 0
    for token in tokens:
        if token['type'] == constTokens.symboleNewLine:
            cpt = cpt + 1
    if cpt < 200:
        print("+1 car nbLignes < 200")
        return 1
    print("-1 car nbLignes >= 200")
    return -1