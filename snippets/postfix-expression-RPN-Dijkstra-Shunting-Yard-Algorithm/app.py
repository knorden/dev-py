nums = '0123456789'
ex = 'A+B*C'
ex = 'a-2+3/4-3*5'
ex = 'hello-2-world'
opDict = { '+' : 10, '-' : 10, '*' : 11, '/' : 11, '^' : 12, }


def make_postfix(exp: str) -> list[str]:
    expression = list(reversed(list(exp)))
    opStack = list()
    postfix = list()

    var = ""
    while len(expression) > 0:
        c = expression.pop()
        if c not in opDict:
            var += c
            if len(expression) == 0:
                postfix += [var]
        else:
            postfix += [var]
            var = ""
            if len(opStack) == 0:
                opStack += c
            else:
                stack_top = opDict[opStack[-1]]
                precedence = opDict[c] - stack_top
                if precedence == 0:
                    postfix += opStack.pop()
                    opStack += c
                elif precedence > 0:
                    opStack += c
                else:
                    while precedence <= 0:
                        if len(opStack) == 0:
                            break
                        precedence = opDict[c] - stack_top
                        o = opStack.pop()
                        postfix += o
                    opStack += c

    while (len(opStack) > 0):
        postfix += opStack.pop()

    return postfix


def make_postfix_bak(exp: str) -> list[str]:
    expression = list(reversed(list(exp)))
    opStack = list()
    postfix = list()

    while len(expression) > 0:
        c = expression.pop()
        if c not in opDict:
            postfix += c
        else:
            if len(opStack) == 0:
                opStack += c
            else:
                stack_top = opDict[opStack[-1]]
                precedence = opDict[c] - stack_top
                if precedence == 0:
                    postfix += opStack.pop()
                    opStack += c
                elif precedence > 0:
                    opStack += c
                else:
                    while precedence <= 0:
                        if len(opStack) == 0:
                            break
                        precedence = opDict[c] - stack_top
                        o = opStack.pop()
                        postfix += o
                    opStack += c

    while (len(opStack) > 0):
        postfix += opStack.pop()

    return postfix

if __name__ == "__main__":
    # ex = input("Enter an expression: ")
    a = make_postfix(ex)
    print(a)
