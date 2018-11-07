import re


def make_grammar(reg):
    if len(reg) == 1:
        if (isupper(reg)):
            return False
        return [('S ->' + reg)]
    if
