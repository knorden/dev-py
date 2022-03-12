nums = '0123456789'
ex = 'A+B*C'
ex = 'a-2+3/4-3*5'

def make_postfix(exp: str) -> list[str]:
    expression = list(reversed(list(exp)))
    print(list(reversed(list(expression))))

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
                precedence = opDict[c] - opDict[opStack[-1]]
                if precedence == 0:
                    postfix += opStack.pop()
                    opStack += c
                elif precedence > 0:
                    opStack += c
                else:
                    print()
                    print("WARNING--------------------")
                    print(f"current operator: {c}")
                    while precedence <= 0:
                        if len(opStack) == 0:
                            break
                        print("PREEEE")
                        print(opStack)
                        print(postfix)
                        precedence = opDict[c] - opDict[opStack[-1]]
                        o = opStack.pop()
                        postfix += o
                        print("POST")
                        print(opStack)
                        print(postfix)
                    print("WARNING--------------------")
                    print()
                    opStack += c
                    continue
        print("This ITER:")
        print(list(reversed(expression)))
        print(postfix)
        print(opStack)
        print()





    # for c in expression:
        # if c not in opDict:
            # var += c
        # else:
            # postfix += [var]
            # var = ""
            # # if:
            # #   - stack not empty, and
            # #   - precedence of incoming operator < one on the stack
            # # then:
            # #   - pop one on stack, append it to postfix.
            # #   - push incoming operator to stack.
            # if len(opStack) > 0 and opDict[c] < opDict[opStack[-1]]:
                # while (len(opStack) > 0):
                    # postfix += opStack.pop()
                # opStack += [c]
            # # other wise,
            # #   - push the operator to the stack.
            # else:
                # opStack += [c]
            # # finally,
            # #   - capture the variable,
            # #   - append it to post fix, and
            # #   - reset it.
    # postfix += [var]

    # finally,
    #   pop all remaining operator from the stack and add to postfix.
    # end = len(opStack)
    # for i in range(end):
    while (len(opStack) > 0):
        postfix += opStack.pop()
    return postfix

if __name__ == "__main__":
    # ex = input("Enter an expression: ")
    a = make_postfix(ex)
    print(a)
