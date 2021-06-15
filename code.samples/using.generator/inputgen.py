# First, create a simple while loop to take input:


class Error(Exception):
    """Base class for other exceptions."""

class EmptyString(Error):
    """Raised when the input is empty."""


def get_nonempty_string(input_type: str):
    while True:
        try:
            inp = input(input_type)
            if len(inp) == 0:
                raise EmptyString
            return inp
        except EmptyString:
            print('Error: empty string input.')


# while True:
    # try:
        # n = input("Enter your code:")
        # if len(n) == 0:
            # raise EmptyString
        # print(f'your entered code: {n}')
        # break
    # except EmptyString:
        # print('Error: empty input.')

a = get_nonempty_string("currency code: ")
