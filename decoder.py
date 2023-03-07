# ANTHONY MADORSKY'S decoding algorithm

def decode(string):
    decoded_string = ""                                 # initialize empty output string
    for letter in string:
        if int(letter) >= 3:
            decoded_string += str(int(letter) - 3)      # decodes (subtracts 3 from) int's 3-9
        else:
            decoded_string += str(int(letter) + 7)      # decodes (adds 7 to) int's 1-2
    return decoded_string