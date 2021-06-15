
data = ['python', 'lowerCamelCase', 'LowerCamelCase']

# goal: convert CamelCase to snake_case
# trick: find the correct place to insert an underscore.                (A)
#       Here we want to insert right before the uppercase letter.
#       For example, for 'lowerCamelCase'
#                         01234567890123
#       We need to insert the underscore at index 5, pertaining to
#       the index of the uppercase letter, then convert the uppercase
#       to lowercase and then append it to the word.
#
#       However, we also must make sure that the first letter is only   (B)
#       converted to uppercase without having an underscore inserted
#       before it.
#
#       So, how do we go about solving this problem.
#       Well, we can start with the two rules: A and B

# def snake_it(input):
    # snake = ''
    # for c in input:
        # if not c.islower():
            # snake += '_' + c.lower()
        # else:
            # snake += c
    # return snake

# def snake_it(s):
    # snake = ''
    # for i, c in enumerate(s):
        # if i == 0:
            # snake += c.lower()
        # else:
            # if not c.islower():
                # snake += '_' + c.lower()
            # else:
                # snake += c
    # return snake

def snake_it(s):
    snake = ''
    for i, c in enumerate(s):
        if i > 0:
            snake += c if c.islower() else '_' + c.lower()
        else:
            snake += c.lower()
    return snake

for st in data:
    print(f"original string : {st} -> {snake_it(st)}")
