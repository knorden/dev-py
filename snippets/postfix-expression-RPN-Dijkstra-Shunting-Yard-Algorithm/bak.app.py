nums = '0123456789'
ex = 'A+B*C'
ex = 'a-2+3/4-3*5'

def make_postfix_bak(exp: str) -> list[str]:
    expression = list(reversed(list(exp)))
    #print(list(reversed(list(expression))))

    opStack = list()
    postfix = list()

    opDict = {
        '+' : 10, '-' : 10, '*' : 11, '/' : 11, '^' : 12,
    }

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
                    #print()
                    #print("WARNING--------------------")
                    #print(f"current operator: {c}")
                    while precedence <= 0:
                        if len(opStack) == 0:
                            break
                        #print("PREEEE")
                        #print(opStack)
                        #print(postfix)
                        precedence = opDict[c] - stack_top
                        o = opStack.pop()
                        postfix += o
                        #print("POST")
                        #print(opStack)
                        #print(postfix)
                    #print("WARNING--------------------")
                    #print()
                    opStack += c
                    continue
        #print("This ITER:")
        #print(list(reversed(expression)))
        #print(postfix)
        #print(opStack)
        #print()
    while (len(opStack) > 0):
        postfix += opStack.pop()
    return postfix


# def make_postfix(exp: str) -> list[str]:
    # expression = list(reversed(list(exp)))
    # opStack = list()
    # postfix = list()

    # opDict = { '+' : 10, '-' : 10, '*' : 11, '/' : 11, '^' : 12, }

    # while len(expression) > 0:
        # c = expression.pop()
        # if c not in opDict:
            # postfix += c
        # else:
            # if len(opStack) == 0:
                # opStack += c
            # else:
                # stack_top = opDict[opStack[-1]]
                # precedence = opDict[c] - stack_top
                # if precedence == 0:
                    # postfix += opStack.pop()
                    # opStack += c
                # elif precedence > 0:
                    # opStack += c
                # else:
                    # while precedence <= 0:
                        # if len(opStack) == 0:
                            # break
                        # precedence = opDict[c] - stack_top
                        # o = opStack.pop()
                        # postfix += o
                    # opStack += c

    # while (len(opStack) > 0):
        # postfix += opStack.pop()

    # return postfix

def make_postfix(exp: str) -> list[str]:
    expression = list(reversed(list(exp)))
    opStack = list()
    postfix = list()

    opDict = { '+' : 10, '-' : 10, '*' : 11, '/' : 11, '^' : 12, }

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
