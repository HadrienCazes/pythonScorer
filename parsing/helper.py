from tokenizer import constants as constTokens
from parsing import constants as constParser

def searchString(tokens, start):
    string=[]
    findend= False
    end= 0
    i = start + 1
    for token in tokens[start+2:]:
        if token['type']==constTokens.symboleQuotationMark:
            findend= True
            end = i
            break
        else:
            string.append(token['value'])
        i = i + 1
    if(not findend):
        raise Exception(constParser.errorMissingQuotationMark)
    return {"type":constParser.typeString, "value": " ".join(string), "start": start, "end": end}

def searchArgs(tokens, start):
    if(tokens[start]['type']!=constTokens.symboleOpenParenthese):
        raise Exception(constParser.errorMissingOpenParenthesis)

    findEnd= False
    end= None
    args= []
    for i in range(start+1,len(tokens)):
        #print(tokens[i])
        if tokens[i]['type']==constTokens.symboleCloseParenthese:
            findEnd= True
            end= i
            #print("BREAK")
            break
        elif tokens[i]['type']==constTokens.typeWord:
            args.append({"type":constParser.typeVariable, "variableName":tokens[i]['value']})
        elif tokens[i]['type']==constTokens.typeNumber:
            args.append(tokens)
        elif tokens[i]['type']==constTokens.symboleQuotationMark:
            temp= searchString(tokens, i)
            args.append(temp)
            i=temp.end

    if(not findEnd):
        raise Exception(constParser.errorMissingCloseParenthesis)
    return {"args": args, "end": end}