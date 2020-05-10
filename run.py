from tokenizer import tokenizer
from parsing.parser import parse

tokens = tokenizer.tokenizer()
parsed = parse(tokens)