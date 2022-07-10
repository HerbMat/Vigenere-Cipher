import argparse
from enum import Enum

from encryptors import VigenereCipher


class Methods(Enum):
    Encrypt = "encrypt"
    Decrypt = "decrypt"


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Encryption details')
    parser.add_argument('--method', type=Methods, default='encrypt', help='method encrypt/decrypt',
                        required=False, metavar='encrypt')
    parser.add_argument('--key', type=str, help='Cipher Key', required=True,
                        metavar='key')
    parser.add_argument('--message', type=str, help='Message Body', required=True,
                        metavar='message')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    vigenereCipher = VigenereCipher()
    key = args.key
    message = args.message.lower()
    if args.method == Methods.Encrypt:
        cipher_text = vigenereCipher.encrypt(key, message)
        print(f"Encrypted message {cipher_text}")
    else:
        plain_text = vigenereCipher.decrypt(key, message)
        print(f"Decrypted message {plain_text}")



