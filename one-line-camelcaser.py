from string import *
def camel_case(s):
    return lower(s[0:s.index(" ")]) + "".join([capitalize(i) for i in (s[s.index(" ")+1:].split())]) if (' ' in s) else s.lower()

if __name__ == "__main__":
    inp = "tHIS is A REAL TEst"
    print inp, "\n", camel_case(inp)
