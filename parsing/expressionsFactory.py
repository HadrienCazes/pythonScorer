from tokenizer import constants as constTokens
from parsing import constants as constParser
from parsing import helper as helper

# def create(tokenType,tokens,start):
#     if tokenType == constParser.expressionMethodCall:
#         return objectMethodCall(tokens,start)
#     else:
#         # pas de declaration de variables , que des affectations
#         # tokenType == constParser.expressionAffectation:
#         return variableAffectation(tokens,start)
#     return None

def create(tokenType,tokens,start):
    if tokenType == constParser.expressionAffectation:
        return variableAffectation(tokens,start)
    else:
        # pas de declaration de variables , que des affectations
        # tokenType == constParser.expressionAffectation:
        return printMethodCall(tokens,start)
    return None

def objectMethodCall(tokens,start):
    objectName = tokens[start]['value']
    if tokens[start+2]['type'] != constTokens.typeWord:
        raise Exception(constParser.errorMissingWord)
    methodName= tokens[start+2]['value']
    arguments = helper.searchArgs(tokens, start+3)
    return {"type": constParser.expressionMethodCall, "objectName": objectName, "methodName":methodName, "arguments": arguments.args, "end": arguments.end}

def variableAffectation(tokens,start):
    if(tokens[start-1]['type'] != constTokens.typeWord):
        raise Exception(constParser.errorMissingWord)
    variableName = tokens[start-1]['value']
    variableValue = None
    if tokens[start+1]['type'] == constTokens.typeNumber or tokens[start+1]['type'] == constTokens.typeWord:
        variableValue = tokens[start+1]
    else:
        if tokens[start+1]['type'] == constTokens.symboleQuotationMark:
            variableValue = helper.searchString(tokens, start+1)
    return {"type": constParser.expressionAffectation, "variableName": variableName, "variableValue": variableValue}

def printMethodCall(tokens,start):
    variableValue = None
    if tokens[start]['type'] != "printFunction":
        raise Exception("not a printFunction!")
    if tokens[start+1]['type'] == constTokens.symboleOpenParenthese and tokens[start+2]['type'] == constTokens.symboleQuotationMark:
        variableValue = helper.searchString(tokens, start+1)
    else:
        variableValue = helper.searchArgs(tokens,start+1)
    return {"type": constParser.expressionPrint,"variableValue": variableValue}