"""
Author: Yuval Hayun
Date: 22/9/2023
Description: this program decrypts and encrypts love letters according to a table of letters that correspond to numbers
and saves the encrypted message in a file that you can later decrypt from and print on a screen
"""
import sys
import logging

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)


FILE_PATH = r"encrypted_msg.txt"
ENCRYPTION_TABLE = {
    'A': '56',
    'B': '57',
    'C': '58',
    'D': '59',
    'E': '40',
    'F': '41',
    'G': '42',
    'H': '43',
    'I': '44',
    'J': '45',
    'K': '46',
    'L': '47',
    'M': '48',
    'N': '49',
    'O': '60',
    'P': '61',
    'Q': '62',
    'R': '63',
    'S': '64',
    'T': '65',
    'U': '66',
    'V': '67',
    'W': '68',
    'X': '69',
    'Y': '10',
    'Z': '11',
    'a': '12',
    'b': '13',
    'c': '14',
    'd': '15',
    'e': '16',
    'f': '17',
    'g': '18',
    'h': '19',
    'i': '30',
    'j': '31',
    'k': '32',
    'l': '33',
    'm': '34',
    'n': '35',
    'o': '36',
    'p': '37',
    'q': '38',
    'r': '39',
    's': '90',
    't': '91',
    'u': '92',
    'v': '93',
    'w': '94',
    'x': '95',
    'y': '96',
    'z': '97',
    ' ': '98',
    ',': '99',
    '.': '100',
    ';': '101',
    '‘': '102',
    '?': '103',
    '!': '104',
    ':': '105'
}
DECRYPTION_TABLE = {
    56: 'A',
    57: 'B',
    58: 'C',
    59: 'D',
    40: 'E',
    41: 'F',
    42: 'G',
    43: 'H',
    44: 'I',
    45: 'J',
    46: 'K',
    47: 'L',
    48: 'M',
    49: 'N',
    60: 'O',
    61: 'P',
    62: 'Q',
    63: 'R',
    64: 'S',
    65: 'T',
    66: 'U',
    67: 'V',
    68: 'W',
    69: 'X',
    10: 'Y',
    11: 'Z',
    12: 'a',
    13: 'b',
    14: 'c',
    15: 'd',
    16: 'e',
    17: 'f',
    18: 'g',
    19: 'h',
    30: 'i',
    31: 'j',
    32: 'k',
    33: 'l',
    34: 'm',
    35: 'n',
    36: 'o',
    37: 'p',
    38: 'q',
    39: 'r',
    90: 's',
    91: 't',
    92: 'u',
    93: 'v',
    94: 'w',
    95: 'x',
    96: 'y',
    97: 'z',
    98: ' ',
    99: ',',
    100: '.',
    101: ';',
    102: '‘',
    103: '?',
    104: '!',
    105: ':'
}


def write_to_file(encrepted_msg):
    """
    writes to file the encrepted message, then closes it
    :param encrepted_msg: the encrepted message to be written to the file ╚(″⚈ᴗ⚈)╗
    :type encrepted_msg: string
    """
    global FILE_PATH
    try:
        text_file = open(FILE_PATH, "w")
        text_file.write(encrepted_msg)
        text_file.close()
    except FileNotFoundError:
        logging.debug("file does't exist")

    except Exception as err:
        logging.error("error in writing file" + str(err))


def read_from_file():
    """
    reads the file and closes it
    :return: returns what is written in the file
    :rtype: str | None
    """
    try:
        text_file = open(FILE_PATH, "r")
        msg = text_file.read()
        text_file.close()
        return msg
    except FileNotFoundError:
        logging.debug("file does't exist")
        return None

    except Exception as err:
        logging.error("error in reading file " + str(err))
        return None


def encrypt(user_msg):
    """
    encrepted the decrepted message from the text file
    :param user_msg:
    :type user_msg: str
    :return: the encrypted message
    :rtype: str
    """
    new_lst = []
    for character in user_msg:
        if character in ENCRYPTION_TABLE.keys():
            new_lst.append(ENCRYPTION_TABLE[character])

    encrypted_msg = ','.join(new_lst)
    logging.debug(user_msg + ' | ' + encrypted_msg + ' | msg has been encrypted successfully')
    return encrypted_msg


def decrypt():
    """
    decrept the encrepted message from the text file
    :return: the decrypted message
    :rtype: str
    """
    decrepted_msg = read_from_file()
    if decrepted_msg == '':
        print("there is nothing to decrypt...乁( ◔ ౪◔)ㄏ")
        return ''
    elif decrepted_msg is None:
        print("file did not exist ")
        return ''
    msg_lst = decrepted_msg.strip().split(',')
    new_lst = []
    for num in msg_lst:
        new_lst.append(DECRYPTION_TABLE[int(num)])
    logging.debug(decrepted_msg + ' | msg has been decrypted successfully')
    return ''.join(new_lst)


def main():
    """
    main function
    """
    if sys.argv[1] == 'encrypt':
        user_msg = input('please enter a love letter please ╚(″⚈ᴗ⚈)╗ : ')
        encrypted_msg = encrypt(user_msg)
        write_to_file(encrypted_msg)

    elif sys.argv[1] == 'decrypt':
        print(decrypt())


if __name__ == '__main__':
    main()
