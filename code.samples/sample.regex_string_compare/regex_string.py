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


def regex(p: Union[str, list], s: Union[str, list], match: int):
    # if len(s) < len(p) or len(p) == 0:
    if len(p) == 0 or len(s) == 0:
        return match

    head_p, rest_p = p[0], p[1::]
    head_s, rest_s = s[0], s[1::]
    if head_p == head_s or head_p == WILDCARDS['DOT']:
        if len(rest_p) > 1 and rest_p[1] == WILDCARDS['QUESTION_MARK'] and head_p and head_s:
            # if rest_p[0] == rest_s[0]:
            print(rest_p, match)
            print(rest_s, match)
            return regex(rest_p[2::], rest_s, match + 3)
            # else:
                # return regex(rest_p[2::], rest_s, match + 2)
        return regex(rest_p, rest_s, match + 1)

        
    else:
        return regex(p, rest_s, match)


def check_regex(p: str, s: str):
    if len(p) > 0:
        if p[0] == WILDCARDS['HEAD'] and p[-1] == WILDCARDS['TAIL']\
                and len(p) < len(s):
            return False
        elif p[0] == '^':
            p = p[1::]
            s = s[:len(p)]
        if p[-1] == '$':
            s = s[::-1][:len(p)]
            p = p[::-1][1::]

    result = regex(p, s, 0)
    valid = [len(p)]
    return True if result in valid else False


if __name__ == "__main__":
    reg = "colou?r"
    sss = "color"

    m = check_regex(reg, sss)
