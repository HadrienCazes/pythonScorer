from tokenizer import constants as constTokens
from parser import constants as constParser
from parser import expressionsFactory as factory

def parser(tokens):
    AST=[]
    for token in tokens:
        expression = None
        if tokens.type == constTokens.typeWord && constParser.declarationVariable.indexOf(tokens[i].value)!=-1){

