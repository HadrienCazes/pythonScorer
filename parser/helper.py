from tokenizer import constants as constTokens
from parser import constants as constParser

def searchString(tokens, start):
    string=[]
    findend= False
    end= 0
    for token in tokens[start+1:]:
        if token==constTokens.symboleQuotationMark:
            findend= True
            end = end + 1
            break
        else:
            string.append(tokens.value)
        end = end + 1  
    if(!findend):
        raise Exception(constParser.errorMissingQuotationMark)
    return {"type":constParser.typeString, "value": string.join(' '), "start": start, "end": end}

def searchArgs(tokens, start):
    if(tokens[start].type!=constTokens.symboleOpenParenthese):
        raise Exception(constParser.errorMissingOpenParenthesis)

    findEnd= False
    end= None
    args= []
    for i in range(start+1,len(tokens)):
        if tokens[i].type==constTokens.symboleCloseParenthese:
            findEnd= True
            end= i
            break
        elif tokens[i].type==constTokens.typeWord:
            args.append({"type":constParser.typeVariable, "variableName":tokens.value})
        elif tokens[i].type==constTokens.typeNumber:
            args.append(tokens)
        elif tokens[i].type==constTokens.symboleQuotationMark:
            temp= searchString(tokens, i)
            args.append(temp)
            i=temp.end

    if(!findEnd):
        raise Exception(constParser.errorMissingCloseParenthesis)
    return {"args": args, "end": end}