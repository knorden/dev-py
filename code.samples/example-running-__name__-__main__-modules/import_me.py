'''This should do some simple tasks.
'''


def say_hi():
    if __name__ == "__main__":
        msg = 'hello world!'
        print(f'{msg}')


if __name__ == "__main__":
    say_hi()
else:
    msg = '- IMPORT_ME:\t Nothing'
    print(f"{msg}, Αγία Σόθια, Κονστάντινόυπολη")
    # print(f"{msg}, not seeing me so I'm not saying hi.")
