"""core of the regex engine.
"""
from typing import Union


# default delimiter between pattern & text
DELIM = '|'
WILDCARDS = {'DOT': '.',
             'HEAD': '^',
             'TAIL': '$',
             'QUESTION_MARK': '?',
             'STAR': '*',
             'PLUS': '+'}


def split_input(uin: str):
    p = uin.index(DELIM)
    r = uin[:p]
    s = uin[p + 1:]
    return r, s


# def check_regex_char(r: Union[list, str], c: Union[list, str]):
#     relation = None
#     if r:
#         if c:
#             if r == c or r[0] == '.':
#                 relation = True
#             elif r != c:
#                 relation = False
#         elif not c:
#             relation = False
#     elif not r:
#         relation = True
#     assert type(relation) is not None, "<relation> must hold a Boolean value"
#     return relation


# def check_string(r, s, prev_relation):
#     if len(s) == 0 or prev_relation is False:
#         return prev_relation
#
#     relation = check_regex_char(r[-1], s[-1])
#     return check_string(r[:-1], s[:-1], relation)


def regex(p: Union[str, list], s: Union[str, list], match: int, pre_cp, pre_cs):
    if len(s) < len(p) or len(p) == 0:
        return match

    head_p, rest_p = p[0], p[1::]
    head_s, rest_s = s[0], s[1::]
    if head_p == head_s or head_p == WILDCARDS['DOT']:
        return regex(rest_p, rest_s, match + 1, head_p, head_s)
    if head_p == WILDCARDS['QUESTION_MARK']:
        print(f"'{WILDCARDS['QUESTION_MARK']}' {p} {s}")
        return regex(rest_p, s, match, head_p, head_s)
    else:
        return regex(p, rest_s, match, head_p, head_s)


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

    result = regex(p, s, 0, "", "")
    valid = [len(p)]
    return True if result in valid else False


def check_all(uin: str):
    pattern, text = split_input(uin)
    result = check_regex(pattern, text)
    print(result)


if __name__ == "__main__":
    print("warning: this module {__name__} explicitly invoked.")
