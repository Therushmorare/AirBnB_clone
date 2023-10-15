import re
from shlex import split

""" function to use for passing arguments"""
def parse(arg):
    """ parse function """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            l_analysis = split(arg[:brackets.span()[0]])
            r_analysis = [i.strip(",") for i in l_analysis]
            re_analysis.append(brackets.group())
            return retl
    else:
        l_analysis = split(arg[:curly_braces.span()[0]])
        re_analysis = [i.strip(",") for i in l_analysis]
        re_analysis.append(curly_braces.group())
        return re_analysis
