# expression = input("enter expression: ").split(' ')
expression = '1 + 2 * 3'
expected = 1 + 2 * 3

print(expression)

op_stack = list()

op_alphabet  = "+-*/"

op_dict = {}
op_dict['+'] = lambda x,y: x + y
op_dict['-'] = lambda x,y: x - y
op_dict['*'] = lambda x,y: x * y
op_dict['/'] = lambda x,y: x / y

num_stack = list()

for c in expression:
    if c in op_alphabet:
        op_stack += [c]
    else:
        num_stack += [int(c)] if c != ' ' else []

print(op_stack)
print(num_stack)

start = num_stack[0]
sum = 0
i = 1

# for op in op_stack:
    # sum = start + op_dict[op](start, num_stack[i])
    # start = sum
    # i += 1

prev = num_stack[-1]

for i in reversed(range(len(op_stack))):
    op = op_stack[i]
    sum = op_dict[op](prev, num_stack[i])
    prev = sum

print(sum)

print(sum == expected)


