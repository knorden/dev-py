nums = '0123456789'
ops = '+-*/'
ex = 'A+B*C'

def make_postfix(exp: str) -> list[str]:
    expression = list(exp)
    opDict = {
    '+' : 10,
    '-' : 10,
    '*' : 11,
    '/' : 11,
    '^' : 12,
    }


    opStack = list()
    postfix = list()

    var = ""
    for c in expression:
        if c not in opDict:
            var += c
        else:
            if len(opStack) > 0 and opDict[c] < opDict[opStack[-1]]:
                postfix += opStack.pop()
            else:
                opStack += [c]
            postfix += [var]
            var = ""

    postfix += [var]

    end = len(opStack)
    for i in range(end):
        postfix += opStack.pop()
    return postfix

if __name__ == "__main__":
    ex = input("Enter an expression: ")
    a = make_postfix(ex)
    print(a)
