import "../tokenizer/constants" as constTokens
import "./constants" as constParser
import "./expressionsFactory" as factory

def parser(tokens):
    AST=[]
    for token in tokens:
        expression = None
        if tokens.type == constTokens.typeWord && constParser.declarationVariable.indexOf(tokens[i].value)!=-1){

