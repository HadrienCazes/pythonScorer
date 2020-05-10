from tokenizer import constants as constTokens
from parsing import constants as constParser
from parsing import expressionsFactory as factory

def parse(tokens):
    print("******************AST***************************************")
    AST=[]
    for i in range(len(tokens)):
        expression = None
        if tokens[i]['type'] == constTokens.symboleEqual:
            expression = factory.create(constParser.expressionAffectation,tokens,i)
            #print(expression)
            if expression['variableValue']['type'] == constTokens.typeNumber or expression['variableValue']['type'] == constTokens.typeWord:
                i=i+1
            # si affectation string on reprend l'analyse après la fermeture des guillements.
            else:
                i=expression['variableValue']['end']
        else:
            # if i<len(tokens)-1 and tokens[i]['type'] == constTokens.typeWord and tokens[i+1]['type']==constTokens.symbolePoint:
            #     expression = factory.create(constParser.expressionMethodCall, tokens, i)
            #     i= expression.end
            if tokens[i]['type'] == "printFunction":
                #print("HERE")
                expression = factory.create(constParser.expressionPrint,tokens,i)
                i = expression['variableValue']['end']
                #print(expression)
        
        if(expression):
            print(expression)
            AST.append(expression)
        else:
            AST.append(tokens[i])
    #print(AST)
    return AST
        
            

