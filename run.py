from tokenizer import tokenizer
from parsing.parser import parse
from scoring.scorer import score 

tokens = tokenizer.tokenizer()
AST = parse(tokens)
score(tokens,AST)