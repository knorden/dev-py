"""regex string check
"""
from typing import Union

DELIM = '|'
WILDCARDS = {'DOT': '.',
             'HEAD': '^',
             'TAIL': '$',
             'QUESTION_MARK': '?',
             'STAR': '*',
             'PLUS': '+'}


# def regex(pattern: Union[str, list], string: Union[str, list], match):
    # # if len(s) < len(p) or len(p) == 0:
    # if len(pattern) == 0 or len(string) == 0:
        # if len(string) < len(pattern):
            # return False
        # return match

    # p, ppp = pattern[0], pattern[1::]
    # s, sss = string[0], string[1::]
    # if p in (s, '.'):
        # if len(ppp) > 1 and ppp[1] == '?':
            # if ppp[0] == sss[0]:
                # return regex(ppp[2::], sss[1::], True)
            # else:
                # return regex(ppp[2::], sss, True)
        # else:
            # return regex(ppp, sss, True)
    # else:
        # if match is True and p != s:
            # return False
        # return regex(ppp, sss, False)


def regex(pattern: Union[str, list], string: Union[str, list], match: int):
    if len(pattern) == 0 or len(string) == 0:
        return match

    p, ppp = pattern[0], pattern[1::]
    s, sss = string[0], string[1::]
    if p in (s, '.'):
        match += 1
        question_mark = 1
        if len(ppp) > 1 and ppp[question_mark] == '?':
            match += 1
            if sss[0] == ppp[0]:
                match += 1
                sss = sss[question_mark::]
                ppp = ppp[question_mark+1::]
            else:
                if sss[0] == ppp[question_mark+1]:
                    match += 1
                    ppp = ppp[question_mark+1::]
                elif sss[0] != ppp[question_mark+1]:
                    match *= -1
                    ppp = []
        return regex(ppp, sss, match) 
    else:
        return regex(pattern, sss, match)


def check_regex(p: str, s: str):
    if len(p) > 0:
        if len(p) < len(s) and p[0] == '^' and p[-1] == '$':
            return False
        if p[0] == '^':
            p = p[1::]
            s = s[:len(p)]
        if p[-1] == '$':
            s = s[::-1][:len(p)]
            p = p[::-1][1::]

    result = regex(p, s, False)
    print(result)
    valid = [len(p)]
    return True if result in valid else False


if __name__ == "__main__":
    reg = "colou?r"
    sss = "colouur"

    m = check_regex(reg, sss)
