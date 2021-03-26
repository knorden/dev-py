'''This is the database (provided tables, and test inputs)
'''

def inf_words():
    """generate an infinite stream of words. Each word is of length 4 chars.
    The fifth symbol is always a space."""
    current = "a"
    nextchar = chr(ord(current) + 1)
    n = 1
    # this is the core loop
    while True:
        yield current
        n += 1
        if n > 4:  # if 5th char, reset the size
            current = " "
            n = 0
        else:  # otherwise, add the next char in the alphabet
            current = nextchar
            nextchar = chr(ord(nextchar) + 1)
            if nextchar > "z":
                nextchar = "a"


# generated ipnut
input2 = inf_words()


ttable2 = {
    "c": "a",
    "d": "b",
    "e": "c",
    "f": "d",
    "g": "e",
    "h": "f",
    "i": "g",
    "j": "h",
    "k": "i",
    "l": "j",
    "m": "k",
    "n": "l",
    "o": "m",
    "p": "n",
    "q": "o",
    "r": "p",
    "s": "q",
    "t": "r",
    "u": "s",
    "v": "t",
    "w": "u",
    "x": "v",
    "y": "w",
    "z": "x",
}


tt1 = {
    "C": "A",
    "D": "B",
    "E": "C",
    "F": "D",
    "G": "E",
    "H": "F",
    "I": "G",
    "J": "H",
    "K": "I",
    "L": "J",
    "M": "K",
    "N": "L",
    "O": "M",
    "P": "N",
    "Q": "O",
    "R": "P",
    "S": "Q",
    "T": "R",
    "U": "S",
    "V": "T",
    "W": "U",
    "X": "V",
    "Y": "W",
    "Z": "X",
    "[": "Y",
    "\\": "Z",
    "c": "a",
    "d": "b",
    "e": "c",
    "f": "d",
    "g": "e",
    "h": "f",
    "i": "g",
    "j": "h",
    "k": "i",
    "l": "j",
    "m": "k",
    "n": "l",
    "o": "m",
    "p": "n",
    "q": "o",
    "r": "p",
    "s": "q",
    "t": "r",
    "u": "s",
    "v": "t",
    "w": "u",
    "x": "v",
    "y": "w",
    "z": "x",
    "{": "y",
    "|": "z",
    "2": "0",
    "3": "1",
    "4": "2",
    "5": "3",
    "6": "4",
    "7": "5",
    "8": "6",
    "9": "7",
    ":": "8",
    ";": "9",
}


ii1 = "R{vjqp ku cp gcu{ vq ngctp, rqygthwn rtqitcookpi ncpiwcig. Kv jcu ghhkekgpv jkij-ngxgn fcvc uvtwevwtgu cpf c ukorng dwv ghhgevkxg crrtqcej vq qdlgev qtkgpvgf-rtqitcookpi. R{vjqp'u gngicpv u{pvcz cpf f{pcoke v{rkpi, vqigvjgt ykvj kvu kpvgtrtgvgf pcvwtg, ocmg kv cp kfgcn ncpiwcig hqt uetkrvkpi cpf tcrkf crrnkecvkqp fgxgnqrogpv kp ocp{ ctgcu qp oquv rncvhqtou."


jj = "r{vq ngctp, rqygthwn"
